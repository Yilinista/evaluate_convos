# Google Forms Empathy Evaluation Project - Memory

## Project Overview
This project creates Google Forms for evaluating empathy in conversational AI chatbots. The forms present conversations between users and a physical activity counselor bot, asking evaluators to rate empathy on 4 dimensions.

## Current Status: COMPLETED ✅
All 55 valid conversations are now distributed across 2 balanced forms ready for deployment.

## Key Requirements Met
1. ✅ Remove unnecessary question blocks from forms
2. ✅ Filter out conversations with insufficient dialogue (now requires ≥4 meaningful turns)
3. ✅ Create 2 balanced sets using ALL available conversations (not just 15 each)
4. ✅ Ensure even distribution of empathy scores between sets
5. ✅ Remove system prompts from displayed conversations
6. ✅ Use clean "Conversation X" titles (not including conversation snippets)
7. ✅ Ensure no duplicate conversations across forms
8. ✅ Manual even distribution (not random sampling) for research validity

## Final Results
- **Total Conversations**: 55 (from 56 after filtering)
- **Set 1**: 28 conversations (1 score-0, 22 score-1, 5 score-2)
- **Set 2**: 27 conversations (0 score-0, 22 score-1, 5 score-2)

## Data Distribution
**Available by Empathy Score:**
- Score 0: 1 conversation (goes to Set 1)
- Score 1: 44 conversations (22 to Set 1, 22 to Set 2)  
- Score 2: 10 conversations (5 to Set 1, 5 to Set 2)

## Files Generated
1. `empathy_form_set1.gs` - Google Apps Script for Form 1
2. `empathy_form_set2.gs` - Google Apps Script for Form 2
3. `conversation_set1_metadata.csv` - Tracking data for Set 1
4. `conversation_set2_metadata.csv` - Tracking data for Set 2
5. `create_improved_forms.py` - Main generation script

## Key Filtering Logic
1. **Conversation Length**: Minimum 4 meaningful turns (ensures proper dialogue)
2. **System Prompt Detection**: Removes prompts like "You are a physical activity counselor..."
3. **Long Message Filter**: Skips messages >500 chars (catches undetected system prompts)
4. **Complete Scores**: Requires all 4 empathy dimension scores present

## Form Structure
Each form contains:
- Instructions for evaluators
- Individual conversation sections with:
  - Clean conversation display (User/Bot format)
  - 4 rating questions (0-2 scale):
    - Emotional Reactions
    - Explorations  
    - Interpretations
    - Overall Empathy

## Conversation Processing
**System Prompt Removal**: Detects and removes prompts containing:
- "You are a physical activity counselor"
- "Please guide the conversation"
- "Here is a summary of your previous session"
- "Motivational Interviewing"
- "The agenda is as follows"
- Messages longer than 500 characters

## Technical Implementation
- **Language**: Python with Google Apps Script generation
- **Distribution Strategy**: Manual even split (not random sampling)
- **Data Source**: 3 rounds of conversation logs from `/evaluated_bot_chats/`
- **Output Format**: JavaScript for Google Forms API

## Issues Resolved
1. ✅ JavaScript syntax errors (quote escaping)
2. ✅ System prompts appearing in conversation data
3. ✅ Random sampling causing uneven distribution
4. ✅ Cluttered conversation titles
5. ✅ Duplicate conversations across forms
6. ✅ Conversations too short for meaningful evaluation

## Usage
To regenerate forms:
```bash
cd /Users/elaine/Downloads/evaluate_convos/google_forms/updated
python create_improved_forms.py
```

This creates ready-to-deploy Google Apps Script files for balanced empathy evaluation research.