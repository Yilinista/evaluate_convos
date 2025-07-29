"""
Google Apps Script Generator for Empathy Evaluation Forms

This script generates Google Apps Script code that creates Google Forms for evaluating 
empathy in chatbot responses. Each form page displays a conversation, LLM scores on 
4 empathy dimensions, and allows human raters to provide their own scores.

The generated script is designed for Prolific user studies comparing human ratings 
with LLM-generated empathy evaluations.
"""

import json
import os
from typing import Dict, List, Any, Tuple

class EmpathyFormGenerator:
    def __init__(self, data_dir: str = "evaluated_bot_chats"):
        self.data_dir = data_dir
        self.empathy_dimensions = [
            "Emotional Reactions",
            "Explorations", 
            "Interpretations",
            "Overall Empathy"
        ]
        
    def load_conversation_data(self) -> Dict[str, List[Tuple[str, Dict]]]:
        """Load conversation data from all rounds."""
        all_conversations = {}
        
        for round_dir in ["round_1", "round_2", "round_3"]:
            round_path = os.path.join(self.data_dir, round_dir)
            if not os.path.exists(round_path):
                continue
                
            message_logs_path = os.path.join(round_path, "message_logs.json")
            if not os.path.exists(message_logs_path):
                continue
                
            with open(message_logs_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            for participant_id, conversation_data in data.items():
                if participant_id not in all_conversations:
                    all_conversations[participant_id] = []
                    
                all_conversations[participant_id].append((round_dir, conversation_data))
                
        return all_conversations
    
    def extract_conversation_text(self, messages: List[Dict]) -> str:
        """Extract and format conversation text for display."""
        conversation_lines = []
        
        for message in messages:
            if message["role"] == "system":
                continue  # Skip system messages in display
            elif message["role"] == "assistant":
                conversation_lines.append(f"**Bot:** {message['content']}")
            elif message["role"] == "user":
                conversation_lines.append(f"**User:** {message['content']}")
                
        return "\n\n".join(conversation_lines)
    
    def get_empathy_scores(self, conversation_data: Dict, session_type: str) -> Dict[str, int]:
        """Extract empathy scores for a specific session."""
        score_keys = {
            "current_session": {
                "emotional_reactions": "current_session_score_emotional_reactions",
                "explorations": "current_session_score_explorations", 
                "interpretations": "current_session_score_interpretations",
                "empathy": "current_session_score_empathy"
            },
            "session_1": {
                "emotional_reactions": "session_1_score_emotional_reactions",
                "explorations": "session_1_score_explorations",
                "interpretations": "session_1_score_interpretations", 
                "empathy": "session_1_score_empathy"
            },
            "session_2": {
                "emotional_reactions": "session_2_score_emotional_reactions",
                "explorations": "session_2_score_explorations",
                "interpretations": "session_2_score_interpretations", 
                "empathy": "session_2_score_empathy"
            },
            "session_3": {
                "emotional_reactions": "session_3_score_emotional_reactions",
                "explorations": "session_3_score_explorations",
                "interpretations": "session_3_score_interpretations", 
                "empathy": "session_3_score_empathy"
            },
            "session_4": {
                "emotional_reactions": "session_4_score_emotional_reactions",
                "explorations": "session_4_score_explorations",
                "interpretations": "session_4_score_interpretations", 
                "empathy": "session_4_score_empathy"
            }
        }
        
        scores = {}
        if session_type in score_keys:
            for dimension, key in score_keys[session_type].items():
                value = conversation_data.get(key)
                # Fix 2: Better type checking for scores
                scores[dimension] = int(value) if isinstance(value, (int, float)) else "N/A"
                
        return scores
    
    def generate_apps_script(self, max_conversations: int = 50) -> str:
        """Generate the complete Google Apps Script code."""
        
        conversations = self.load_conversation_data()
        
        # Flatten and limit conversations for the form
        form_conversations = []
        conversation_count = 0
        skipped_conversations = 0
        
        for participant_id, rounds in conversations.items():
            for round_name, conversation_data in rounds:
                # Process all sessions that have empathy scores
                session_types = ["current_session", "session_1", "session_2", "session_3", "session_4"]
                
                for session_type in session_types:
                    if conversation_count >= max_conversations:
                        break
                        
                    if session_type in conversation_data:
                        session_text = self.extract_conversation_text(
                            conversation_data[session_type]
                        )
                        session_scores = self.get_empathy_scores(conversation_data, session_type)
                        
                        if session_text.strip() and any(isinstance(v, int) for v in session_scores.values()):
                            form_conversations.append({
                                "id": f"{participant_id}_{round_name}_{session_type}",
                                "participant": participant_id,
                                "round": round_name,
                                "session": session_type,
                                "text": session_text,
                                "llm_scores": session_scores
                            })
                            conversation_count += 1
                        else:
                            skipped_conversations += 1
            
            # Fix 4: Move the outer break here for better flow control  
            if conversation_count >= max_conversations:
                break
        
        print(f"Processed {conversation_count} conversations, skipped {skipped_conversations} (missing text or scores)")
        
        # Generate the Apps Script code
        script_code = self._generate_script_template(form_conversations)
        return script_code
    
    def _generate_script_template(self, conversations: List[Dict]) -> str:
        """Generate the Google Apps Script template."""
        
        conversations_js = json.dumps(conversations, indent=2)
        
        script = f'''/**
 * Google Apps Script: Empathy Evaluation Form Generator
 * 
 * This script creates a Google Form for evaluating empathy in chatbot responses.
 * It compares LLM-generated empathy scores with human rater evaluations.
 * 
 * Instructions:
 * 1. Open Google Apps Script (script.google.com)
 * 2. Create a new project
 * 3. Replace the default code with this script
 * 4. Run the 'createEmpathyEvaluationForm' function
 * 5. Check your Google Drive for the generated form
 */

function createEmpathyEvaluationForm() {{
  // Form configuration
  const FORM_TITLE = "🤖 Chatbot Empathy Evaluation Study";
  const FORM_DESCRIPTION = `
Welcome to our research study on empathy in AI conversations! 👋

**What you'll do:**
• Review conversations between users and a physical activity counselor chatbot
• Rate the chatbot's empathy on 4 key dimensions (0-2 scale)
• Share your confidence level and optional feedback

**Time required:** Approximately 15-20 minutes
**Number of conversations:** ${{conversations.length}}

Your thoughtful evaluation will help us understand how well AI systems can demonstrate empathy in supportive conversations.

Thank you for contributing to this important research! 🙏
  `.trim();

  // Conversation data from your pilot study
  const conversations = {conversations_js};
  
  // Create the form
  const form = FormApp.create(FORM_TITLE);
  form.setDescription(FORM_DESCRIPTION);
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setLimitOneResponsePerUser(false);
  
  // Add conversation evaluation pages directly
  conversations.forEach((conversation, index) => {{
    addConversationPage(form, conversation, index + 1, conversations.length);
  }});
  
  // Add final page
  addFinalPage(form);
  
  // Set up form settings
  form.setConfirmationMessage("Thank you for participating in our empathy evaluation study! Your responses have been recorded.");
  
  // Log the form URL
  const formUrl = form.getPublishedUrl();
  console.log("Form created successfully!");
  console.log("Form URL: " + formUrl);
  console.log("Edit URL: " + form.getEditUrl());
  
  return form;
}}

function addConsentPage(form) {{
  form.addPageBreakItem()
    .setTitle("Informed Consent")
    .setHelpText(`
This research study is examining how people evaluate empathy in chatbot conversations. 

By participating, you agree that:
- Your responses will be used for research purposes
- Your data will be kept confidential and anonymous
- You can withdraw at any time
- You are 18 years or older

Do you consent to participate in this study?
    `.trim());
    
  form.addMultipleChoiceItem()
    .setTitle("Consent to Participate")
    .setChoices([
      form.createChoice("Yes, I consent to participate"),
      form.createChoice("No, I do not consent")
    ])
    .setRequired(true);
}}

function addDemographicQuestions(form) {{
  form.addPageBreakItem()
    .setTitle("Background Information")
    .setHelpText("Please provide some basic information about yourself.");
    
  // Age range
  form.addMultipleChoiceItem()
    .setTitle("What is your age range?")
    .setChoices([
      form.createChoice("18-24"),
      form.createChoice("25-34"), 
      form.createChoice("35-44"),
      form.createChoice("45-54"),
      form.createChoice("55-64"),
      form.createChoice("65+")
    ])
    .setRequired(true);
    
  // Experience with chatbots
  form.addScaleItem()
    .setTitle("How familiar are you with chatbots or AI assistants?")
    .setBounds(1, 5)
    .setLabels("Not at all familiar", "Very familiar")
    .setRequired(true);
    
  // Professional background
  form.addTextItem()
    .setTitle("What is your professional background or field of work? (Optional)")
    .setRequired(false);
}}

function addConversationPage(form, conversation, pageNumber, totalConversations) {{
  const pageTitle = `📋 Conversation ${{pageNumber}} of ${{totalConversations}}`;
  const conversationId = conversation.id;
  
  // Clean up participant ID display
  const participantDisplay = conversation.participant.replace('whatsapp:+', 'P-');
  const sessionDisplay = conversation.session.replace('_', ' ').replace(/\\b\\w/g, l => l.toUpperCase());
  
  form.addPageBreakItem()
    .setTitle(pageTitle)
    .setHelpText(`
📊 **Study Context**
• Participant ID: ${{participantDisplay}}
• Study Round: ${{conversation.round.replace('_', ' ').toUpperCase()}}  
• Session Type: ${{sessionDisplay}}

📖 **Instructions:** Please read the conversation below carefully, then rate the chatbot's empathy on four dimensions.
    `.trim());
  
  // Display the conversation with better formatting
  form.addSectionHeaderItem()
    .setTitle("💬 Conversation Transcript");
    
  // Improved conversation display with better formatting
  const formattedConversation = conversation.text
    .replace(/\\*\\*Bot:\\*\\*/g, '🤖 **Chatbot:**')
    .replace(/\\*\\*User:\\*\\*/g, '�� **User:**');
    
  form.addParagraphTextItem()
    .setTitle("Conversation")
    .setHelpText(`<div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6;"><pre style="white-space: pre-wrap; margin: 0;">${{formattedConversation}}</pre></div>`)
    .setRequired(false);
  
  // Human evaluation grid with better styling
  form.addSectionHeaderItem()
    .setTitle("🎯 Your Empathy Assessment");
    
  form.addParagraphTextItem()
    .setTitle("📝 Rating Guidelines")
    .setHelpText(`
**Please rate the chatbot's empathy on each dimension:**

🔹 **0 = Not Present** - The chatbot shows no evidence of this empathy dimension
🔹 **1 = Somewhat Present** - The chatbot shows some evidence but it's limited or unclear  
🔹 **2 = Strongly Present** - The chatbot clearly demonstrates this empathy dimension

**📚 Dimension Definitions:**
• **Emotional Reactions**: Does the chatbot express warmth, compassion, concern, or similar supportive feelings?
• **Explorations**: Does the chatbot actively explore and inquire about the user's experiences and feelings?
• **Interpretations**: Does the chatbot demonstrate understanding by reflecting or paraphrasing the user's situation?
• **Overall Empathy**: Does the chatbot show overall emotional understanding and connection with the user?
    `.trim())
    .setRequired(false);
  
  // Create empathy rating grid with better labels
  const empathyGrid = form.addGridItem();
  empathyGrid.setTitle(`⭐ Empathy Ratings - Conversation ${{pageNumber}}`);
  empathyGrid.setRows([
    "🔸 Emotional Reactions",
    "🔸 Explorations", 
    "🔸 Interpretations",
    "🔸 Overall Empathy"
  ]);
  empathyGrid.setColumns(["0 (Not Present)", "1 (Somewhat Present)", "2 (Strongly Present)"]);
  empathyGrid.setRequired(true);
  
  // Add confidence rating with better styling
  form.addScaleItem()
    .setTitle("🎯 Confidence Level: How confident are you in your empathy ratings above?")
    .setBounds(1, 5)
    .setLabels("Not confident at all", "Very confident")
    .setRequired(true);
  
  // Optional comments with better prompt
  form.addParagraphTextItem()
    .setTitle("💭 Additional Comments (Optional)")
    .setHelpText("Feel free to share any thoughts about this conversation or explain your reasoning for the ratings above.")
    .setRequired(false);
}}

function addFinalPage(form) {{
  form.addPageBreakItem()
    .setTitle("Study Complete")
    .setHelpText(`
Thank you for participating in our empathy evaluation study!

Your responses will help us understand how humans and AI systems evaluate empathy in conversations.

If you have any questions about this research, please contact the research team.
    `.trim());
    
  form.addParagraphTextItem()
    .setTitle("Final feedback")
    .setHelpText("Do you have any final thoughts about this study or the conversations you evaluated? (Optional)")
    .setRequired(false);
}}

// Function to validate and test the form creation
function testFormCreation() {{
  try {{
    const form = createEmpathyEvaluationForm();
    console.log("Form created successfully with " + form.getItems().length + " items");
  }} catch (error) {{
    console.error("Error creating form:", error);
  }}
}}
'''
        
        return script
    
    def save_script_to_file(self, script_code: str, filename: str = "empathy_evaluation_form.gs"):
        """Save the generated script to a file."""
        # Fix 1: Add folder check when saving script
        output_dir = "google_forms"
        os.makedirs(output_dir, exist_ok=True)
        
        script_path = os.path.join(output_dir, filename)
        
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_code)
        
        print(f"Google Apps Script saved to: {script_path}")
        return script_path

def main():
    """Main function to generate the empathy evaluation form script."""
    generator = EmpathyFormGenerator()
    
    print("Loading conversation data...")
    conversations = generator.load_conversation_data()
    print(f"Found conversations for {len(conversations)} participants")
    
    print("Generating Google Apps Script...")
    script_code = generator.generate_apps_script(max_conversations=100)  # Increase to capture all available
    
    print("Saving script file...")
    script_path = generator.save_script_to_file(script_code)
    
    print("\n" + "="*60)
    print("GOOGLE APPS SCRIPT GENERATED SUCCESSFULLY!")
    print("="*60)
    print(f"Script saved to: {script_path}")
    print("\nNext steps:")
    print("1. Open Google Apps Script (script.google.com)")
    print("2. Create a new project")
    print("3. Copy the generated script code")
    print("4. Run the 'createEmpathyEvaluationForm' function")
    print("5. Check your Google Drive for the form")
    print("6. Share the form URL with Prolific participants")
    
    return script_path

if __name__ == "__main__":
    main()
