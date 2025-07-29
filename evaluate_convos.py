import openai
import json
import os
import dotenv
import google.generativeai as genai
import re

dotenv.load_dotenv(".env")

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# for model in genai.list_models():
#     print(f"Model Name: {model.name}")
#     print(f"  Description: {model.description}")
#     print(f"  Supported Generation Methods: {model.supported_generation_methods}")
#     print("-" * 30)

# client = openai.OpenAI()

def load_prompt_template(model_name): 
  path=None
  if model_name == "gemini": 
    path="empathy-evaluation-prompt-gemini.txt"
  else: # gemini
    path="empathy-evaluation-prompt.txt"
  
  with open(path, "r", encoding="utf-8") as f: 
      return f.read()

# static items required for conversation evaluation
MODEL = "gpt-4.1"
INPUT_ROOT = os.path.join(os.getcwd(), "bot_chats")
OUTPUT_ROOT = os.path.join(os.getcwd(), "evaluated_bot_chats")
# change this to "gpt" or "gemini" to load LLM specific prompt
PROMPT_TEMPLATE = load_prompt_template("gemini")

def format_conversation(convo_list): 
  lines = []
  for item in convo_list: 
    line = f"{item['role']}: {item['content']}"
    lines.append(line)
  
  return "\n".join(lines)

def get_empathy_score_gpt(convo_text): 
  try: 
    response = client.chat.completions.create(
      model=MODEL,
      messages=[
        {"role": "system", "content": "You are an empathy evaluator."},
        {"role": "user", "content": PROMPT_TEMPLATE.format(conversation=convo_text)}
      ],
      temperature=0
    )
    score_str = response.choices[0].message.content.strip()
    score = int(score_str)
    return max(0, min(score, 5))  # Clamp to [0, 5]
  except Exception as e: 
    print(e)
    return None

def extract_json_block(text):
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        return match.group(0)
    return None

def get_empathy_score_gemini(conversation, model=None):
    if model is None:
        model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = f"""
You are an expert empathy evaluator. Given the following conversation, assess the quality of the response on the following four dimensions. Use a 0–2 scale (0 = not at all, 1 = somewhat, 2 = strongly present).

Definitions:
1. **Emotional Reactions**: Does the response express or allude to warmth, compassion, concern, or similar feelings of the responder towards the seeker?
2. **Explorations**: Does the response make an attempt to explore the seeker’s experiences and feelings?
3. **Interpretations**: Does the response communicate an understanding of the seeker’s experiences and feelings?
4. **Empathy**: Did the response demonstrate an understanding of the feelings of the person sharing their experience?

Conversation:
{conversation}

Return the scores in this JSON format only:
{{
  "emotional_reactions": 1,
  "explorations": 2,
  "interpretations": 1,
  "empathy": 2
}}
"""

    try:
        response = model.generate_content(prompt)
        score_text = response.text.strip()

        print("\n🔍 RAW GEMINI OUTPUT:")
        print(score_text)

        score_json = extract_json_block(score_text)
        if not score_json:
            raise ValueError("❌ No valid JSON block found in Gemini response.")

        parsed_score = json.loads(score_json)

        for field in ["emotional_reactions", "explorations", "interpretations", "empathy"]:
            if field not in parsed_score:
                raise ValueError(f"❌ Missing field: {field} in parsed response.")

        return parsed_score

    except Exception as e:
        print(f"\n🛑 Error in Gemini evaluation: {e}")
        return None

def process_round(round_path, round_name): 
  input_file = os.path.join(round_path, "message_logs.json")
  if not os.path.isfile(input_file): 
    print(f"{input_file} is missing, skipping...")
  
  with open(input_file, "r", encoding="utf-8") as f: 
    data = json.load(f)
  
  for phone, sessions, in data.items(): 
    # list takes a snapshot of the keys and doesn't affect the loop if more keys are added later
    for session_key, convo in list(sessions.items()):
      convo = sessions[session_key] 
      if isinstance(convo, list): 
        convo_text = format_conversation(convo)
        print(f"EVALUATING {round_name} | {phone} | {session_key}")
        # replace this with gpt or gemini depending on the evaluation LLM
        score = get_empathy_score_gemini(convo_text)
        if score is not None: 
          for k, v in score.items():
              sessions[f"{session_key}_score_{k}"] = v


  
  data["round"] = round_name
  
  output_dir = os.path.join(OUTPUT_ROOT, round_name)
  os.makedirs(output_dir, exist_ok=True)
  output_path = os.path.join(output_dir, "message_logs.json")
  
  with open(output_path, "w", encoding="utf-8") as f: 
    json.dump(data, f, indent=2, ensure_ascii=False)
  
  print(f"Save evaluated file to output_path {output_path}")

def main(): 
  if not os.path.exists(INPUT_ROOT): 
    print(f"INPUT folder {INPUT_ROOT} not found")
    return
  
  for entry in os.listdir(INPUT_ROOT): 
    round_path = os.path.join(INPUT_ROOT, entry)
    if os.path.isdir(round_path) and entry.startswith("round_"): 
      process_round(round_path, entry)

if __name__ == "__main__": 
  main()
  