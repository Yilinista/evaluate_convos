import json
import os
from collections import defaultdict
import random
import csv

class ImprovedFormGenerator:
    def __init__(self, data_path="../evaluated_bot_chats"):
        self.data_path = data_path
        self.all_conversations = []
        
    def load_and_filter_conversations(self):
        """Load conversations and filter out single-turn conversations"""
        conversations = []
        
        for round_folder in ["round_1", "round_2", "round_3"]:
            round_path = os.path.join(self.data_path, round_folder, "message_logs.json")
            if not os.path.exists(round_path):
                print(f"Warning: {round_path} not found")
                continue
                
            with open(round_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            round_name = data.get("round", round_folder)
            
            for participant_id, sessions in data.items():
                if participant_id == "round":
                    continue
                    
                # Process each session
                session_keys = [k for k in sessions.keys() if not k.endswith('_score_emotional_reactions') 
                               and not k.endswith('_score_explorations')
                               and not k.endswith('_score_interpretations') 
                               and not k.endswith('_score_empathy')]
                
                for session_key in session_keys:
                    convo = sessions.get(session_key, [])
                    
                    # Skip if not a conversation list or too short
                    if not isinstance(convo, list) or len(convo) <= 1:
                        continue
                    
                    # Count meaningful turns (excluding system prompts)
                    meaningful_turns = 0
                    for turn in convo:
                        if turn['role'] == 'system':
                            continue
                        if turn['role'] == 'user':
                            content = turn['content']
                            # Skip system-like user messages
                            if ('You are a physical activity counselor' in content or
                                'Please guide the conversation' in content or
                                'Here is a summary of your previous session' in content or
                                'Motivational Interviewing' in content or
                                'The agenda is as follows' in content or
                                len(content) > 500):
                                continue
                        meaningful_turns += 1
                    
                    # Require at least 4 meaningful turns for proper back-and-forth dialogue
                    if meaningful_turns < 4:
                        continue
                    
                    # Get scores for this session
                    scores = {
                        'emotional_reactions': sessions.get(f"{session_key}_score_emotional_reactions"),
                        'explorations': sessions.get(f"{session_key}_score_explorations"),
                        'interpretations': sessions.get(f"{session_key}_score_interpretations"),
                        'empathy': sessions.get(f"{session_key}_score_empathy")
                    }
                    
                    # Skip if any score is missing
                    if any(score is None for score in scores.values()):
                        continue
                    
                    # Calculate average score
                    avg_score = sum(scores.values()) / len(scores)
                    
                    conversations.append({
                        'round': round_name,
                        'participant_id': participant_id,
                        'session_key': session_key,
                        'conversation': convo,
                        'scores': scores,
                        'avg_score': avg_score,
                        'turn_count': len(convo)
                    })
        
        self.all_conversations = conversations
        print(f"Loaded {len(conversations)} multi-turn conversations with complete scores")
        return conversations
    
    def stratified_sample(self, conversations, n_per_category=5):
        """Create stratified sample with even distribution across score categories"""
        # Categorize by rounded average score (0, 1, or 2)
        categorized = defaultdict(list)
        
        for conv in conversations:
            # Round average score to nearest integer (0, 1, or 2)
            category = round(conv['avg_score'])
            category = max(0, min(2, category))  # Ensure it's within 0-2
            categorized[category].append(conv)
        
        sampled_conversations = []
        
        for category in [0, 1, 2]:
            available = categorized[category]
            if len(available) >= n_per_category:
                sampled = random.sample(available, n_per_category)
            else:
                # If not enough conversations in this category, take all available
                sampled = available
                print(f"Warning: Only {len(available)} conversations available for category {category}")
            
            sampled_conversations.extend(sampled)
        
        # Shuffle the final sample
        random.shuffle(sampled_conversations)
        return sampled_conversations
    
    def create_conversation_sets(self, n_sets=2):
        """Create multiple sets including ALL conversations with even distribution"""
        # Categorize all conversations by empathy score
        categorized = defaultdict(list)
        
        for conv in self.all_conversations:
            # Use the empathy score directly instead of average
            empathy_score = conv['scores']['empathy']
            categorized[empathy_score].append(conv)
        
        # Print available conversations by category
        print("\nAvailable conversations by empathy score:")
        for score in [0, 1, 2]:
            print(f"  Score {score}: {len(categorized[score])} conversations")
        
        # Manual distribution for even sets - include ALL conversations
        sets = []
        
        # Set 1 and Set 2 lists
        set1_conversations = []
        set2_conversations = []
        
        # Distribute each score category as evenly as possible between sets
        for score in [0, 1, 2]:
            conversations = categorized[score]
            mid_point = len(conversations) // 2
            
            # Set 1 gets first half (or half + 1 if odd number)
            set1_conversations.extend(conversations[:mid_point + (len(conversations) % 2)])
            
            # Set 2 gets second half
            set2_conversations.extend(conversations[mid_point + (len(conversations) % 2):])
        
        # Shuffle each set to randomize order within the set
        random.shuffle(set1_conversations)
        random.shuffle(set2_conversations)
        
        sets.append({
            'set_number': 1,
            'conversations': set1_conversations
        })
        
        sets.append({
            'set_number': 2, 
            'conversations': set2_conversations
        })
        
        return sets
    
    def format_conversation_for_display(self, conversation):
        """Format conversation for clear display in form"""
        lines = []
        skip_first_user = False
        
        # Check if first message is a system prompt
        if conversation and conversation[0]['role'] in ['user', 'system']:
            first_msg = conversation[0]['content']
            # If the first message contains prompt indicators, skip it
            if ('You are a physical activity counselor' in first_msg or
                'Please guide the conversation' in first_msg or
                'Here is a summary of your previous session' in first_msg or
                'Motivational Interviewing' in first_msg or
                'The agenda is as follows' in first_msg or
                len(first_msg) > 500):
                skip_first_user = True
        
        for i, turn in enumerate(conversation):
            # Skip the first user message if it's a system prompt
            if i == 0 and skip_first_user:
                continue
                
            role = "Bot" if turn['role'] == 'assistant' else "User"
            content = turn['content'].strip().replace('"', '\\"').replace("'", "\\'")
            lines.append(f"{role}: {content}")
        return "\\n\\n".join(lines)
    
    def generate_form_script(self, conversation_set, set_number):
        """Generate Google Apps Script for a specific conversation set"""
        
        script_template = '''function createEmpathyEvaluationForm_Set{set_number}() {{
  // Create form
  var form = FormApp.create('Empathy Evaluation - Set {set_number}');
  
  // Add instructions
  form.setDescription(
    'Please evaluate the following conversations between a user and a chatbot. ' +
    'Rate each conversation on four dimensions of empathy using the scale provided.\\n\\n' +
    'Scale: 0 = Not at all, 1 = Somewhat, 2 = Strongly present'
  );
  
  // Add conversations
  {conversation_sections}
  
  // Log form URL
  Logger.log('Form URL: ' + form.getPublishedUrl());
  Logger.log('Edit URL: ' + form.getEditUrl());
}}

{conversation_data}
'''

        conversation_sections = []
        conversation_data_sections = []
        
        for idx, conv_data in enumerate(conversation_set['conversations']):
            conv_id = f"conv_{idx + 1}"
            conversation_text = self.format_conversation_for_display(conv_data['conversation'])
            
            # Create a title from first actual user message (not the prompt)
            # Check if first message is a system prompt
            skip_first = False
            if conv_data['conversation'] and conv_data['conversation'][0]['role'] in ['user', 'system']:
                first_msg = conv_data['conversation'][0]['content']
                if ('You are a physical activity counselor' in first_msg or
                    'Please guide the conversation' in first_msg or
                    'Here is a summary of your previous session' in first_msg or
                    'Motivational Interviewing' in first_msg or
                    'The agenda is as follows' in first_msg or
                    len(first_msg) > 500):
                    skip_first = True
            
            # Find the first real user message
            first_user_msg = ""
            start_idx = 1 if skip_first else 0
            
            for i in range(start_idx, len(conv_data['conversation'])):
                turn = conv_data['conversation'][i]
                if turn['role'] == 'user':
                    first_user_msg = turn['content'][:50].replace("'", "\\'") + "..."
                    break
            
            # If no user message found, use first bot message
            if not first_user_msg:
                for turn in conv_data['conversation']:
                    if turn['role'] == 'assistant':
                        first_user_msg = "Bot: " + turn['content'][:45].replace("'", "\\'") + "..."
                        break
            
            # Fallback to generic title
            if not first_user_msg:
                first_user_msg = f"Conversation about physical activity"
            
            section = f'''
  // Conversation {idx + 1}
  form.addPageBreakItem()
    .setTitle('Conversation {idx + 1}');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation {idx + 1}')
    .setHelpText(conversationData['{conv_id}'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);'''
            
            conversation_sections.append(section)
            
            # Add conversation data
            # Replace newlines with escaped newlines for JavaScript
            js_safe_text = conversation_text.replace('\n', '\\n')
            data_section = f'''
  '{conv_id}': {{
    text: "{js_safe_text}",
    participant_id: "{conv_data['participant_id']}",
    session: "{conv_data['session_key']}",
    round: "{conv_data['round']}",
    llm_scores: {{
      emotional_reactions: {conv_data['scores']['emotional_reactions']},
      explorations: {conv_data['scores']['explorations']},
      interpretations: {conv_data['scores']['interpretations']},
      empathy: {conv_data['scores']['empathy']}
    }}
  }}'''
            conversation_data_sections.append(data_section)
        
        # Build the conversation data object
        conversation_data = "var conversationData = {" + ",".join(conversation_data_sections) + "\n};"
        
        return script_template.format(
            set_number=set_number,
            conversation_sections="\n".join(conversation_sections),
            conversation_data=conversation_data
        )
    
    def save_conversation_csv(self, conversation_set, filename):
        """Save conversation metadata to CSV for tracking"""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'index', 'participant_id', 'session', 'round', 
                'turn_count', 'avg_llm_score',
                'emotional_reactions', 'explorations', 'interpretations', 'empathy'
            ])
            
            for idx, conv in enumerate(conversation_set['conversations']):
                writer.writerow([
                    idx + 1,
                    conv['participant_id'],
                    conv['session_key'],
                    conv['round'],
                    conv['turn_count'],
                    round(conv['avg_score'], 2),
                    conv['scores']['emotional_reactions'],
                    conv['scores']['explorations'],
                    conv['scores']['interpretations'],
                    conv['scores']['empathy']
                ])

def main():
    # Initialize generator
    generator = ImprovedFormGenerator()
    
    # Load and filter conversations
    generator.load_and_filter_conversations()
    
    # Create 2 sets including ALL conversations
    conversation_sets = generator.create_conversation_sets(n_sets=2)
    
    # Generate scripts and CSVs for each set
    for conv_set in conversation_sets:
        set_number = conv_set['set_number']
        
        # Generate Google Apps Script
        script = generator.generate_form_script(conv_set, set_number)
        script_filename = f"empathy_form_set{set_number}.gs"
        with open(script_filename, 'w', encoding='utf-8') as f:
            f.write(script)
        print(f"Generated {script_filename}")
        
        # Save CSV for tracking
        csv_filename = f"conversation_set{set_number}_metadata.csv"
        generator.save_conversation_csv(conv_set, csv_filename)
        print(f"Generated {csv_filename}")
        
        # Print summary statistics
        scores = [c['avg_score'] for c in conv_set['conversations']]
        print(f"\nSet {set_number} Statistics:")
        print(f"  Total conversations: {len(conv_set['conversations'])}")
        print(f"  Score distribution:")
        for score in [0, 1, 2]:
            count = sum(1 for c in conv_set['conversations'] if round(c['avg_score']) == score)
            print(f"    Score ~{score}: {count} conversations")
        print(f"  Average score: {sum(scores)/len(scores):.2f}")
        print(f"  Score range: {min(scores):.2f} - {max(scores):.2f}")

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)
    main()