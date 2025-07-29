import pandas as pd
import json
from pathlib import Path

def reload_survey_data_with_chat():
    """Reload survey data with ALL metrics and add chat engagement data"""
    
    survey_files = [
        ('../survey_forms/Physical Activity Chatbot Form (Responses).xlsx', 'main'),
        ('../survey_forms/Physical Activity Chatbot Form - NE (Responses).xlsx', 'ne'),
        ('../survey_forms/Physical Activity Chatbot Form - Normal (Responses).xlsx', 'normal')
    ]
    
    all_participants = []
    
    for file, survey_type in survey_files:
        df = pd.read_excel(file)
        activity_col = 'Please select the one that describes your current physical activity status'
        
        # Filter for 'not physically active' participants
        not_active = df[df[activity_col].str.contains('not physically active', na=False)]
        
        for _, row in not_active.iterrows():
            # Extract ALL available metrics with CORRECT column names
            participant_data = {
                'prolific_id': row['Your Prolific ID'],
                'survey_type': survey_type,
                'physical_activity_status': row.get(activity_col),
                'satisfaction': row.get('How would you rate your overall satisfaction with this computer program?'),
                'enjoyment': row.get('How much did you enjoy using this computer program?'),
                'ease_of_use': row.get('How easy was this computer program for you to use?'),
                'naturalistic': row.get('Did the chatbot provide naturalistic responses?'),
                'useful': row.get("I think the chatbot's recommendation is useful for enhancing my physical activity"),
                'intent_to_follow': row.get("I intend to follow the chatbot's recommendation over the next 7 days"),
                'confidence': row.get("If I do intend to follow the chatbot's recommendation, I am confident that I can follow the recommendation over the next 7 days"),
                'time_acceptable': row.get('Was the amount of time it took to complete this computer program acceptable?'),
                'understandable': row.get('How understandable were the questions?')
            }
            all_participants.append(participant_data)
    
    return pd.DataFrame(all_participants)

def add_chat_engagement(df):
    """Add chat engagement data from message logs"""
    
    def analyze_chat_engagement(prolific_id, phone_number):
        rounds = ["round_1", "round_2", "round_3"]
        base_dir = Path("../bot_chats")
        
        total_messages = 0
        total_user_messages = 0
        avg_message_length = 0
        
        for rnd in rounds:
            round_dir = base_dir / rnd
            
            try:
                with open(round_dir / "message_logs.json") as f:
                    logs = json.load(f)
                    
                phone_key = f"whatsapp:{phone_number}"
                if phone_key in logs:
                    for session_key, messages in logs[phone_key].items():
                        if isinstance(messages, list):
                            for msg in messages:
                                if isinstance(msg, dict) and msg.get('role') == 'user':
                                    total_user_messages += 1
                                    total_messages += 1
                                    avg_message_length += len(msg.get('content', ''))
                                elif isinstance(msg, dict) and msg.get('role') == 'assistant':
                                    total_messages += 1
                                    
            except (FileNotFoundError, json.JSONDecodeError, KeyError):
                continue
        
        if total_user_messages > 0:
            avg_message_length = avg_message_length / total_user_messages
        
        return {
            'total_messages': total_messages,
            'user_messages': total_user_messages,
            'avg_message_length': avg_message_length
        }
    
    # Load chat mappings
    def map_to_chat_conditions():
        rounds = ["round_1", "round_2", "round_3"]
        base_dir = Path("../bot_chats")
        
        all_mappings = {}
        
        for rnd in rounds:
            round_dir = base_dir / rnd
            
            try:
                with open(round_dir / "exp_id_map.json") as f:
                    exp_id_map = json.load(f)
                    
                for phone, (prolific_id, condition) in exp_id_map.items():
                    if prolific_id not in all_mappings:
                        all_mappings[prolific_id] = {
                            'condition': condition,
                            'phone': phone.replace('whatsapp:', '')
                        }
            except FileNotFoundError:
                continue
        
        return all_mappings
    
    chat_mappings = map_to_chat_conditions()
    
    # Add chat engagement data
    engagement_data = []
    for _, participant in df.iterrows():
        prolific_id = participant['prolific_id']
        chat_info = chat_mappings.get(prolific_id, {})
        phone = chat_info.get('phone', '')
        
        if phone:
            engagement = analyze_chat_engagement(prolific_id, phone)
        else:
            engagement = {'total_messages': 0, 'user_messages': 0, 'avg_message_length': 0}
        
        engagement_data.append(engagement)
    
    # Add engagement columns to dataframe
    for key in ['total_messages', 'user_messages', 'avg_message_length']:
        df[key] = [data[key] for data in engagement_data]
    
    return df

def main():
    print("🔧 FIXING COMPLETE DATA EXTRACTION")
    print("=" * 50)
    
    # Reload survey data with all metrics
    df = reload_survey_data_with_chat()
    
    # Add correct condition mapping
    condition_map = {
        'main': 'Empathetic',
        'ne': 'Non-Empathetic', 
        'normal': 'Normal'
    }
    df['condition'] = df['survey_type'].map(condition_map)
    
    # Add chat engagement data
    df = add_chat_engagement(df)
    
    print(f"✅ Complete data for {len(df)} non-physically active participants:")
    print("\nKey metrics check:")
    key_cols = ['prolific_id', 'condition', 'satisfaction', 'enjoyment', 'useful', 'intent_to_follow', 'confidence', 'user_messages']
    print(df[key_cols].to_string(index=False))
    
    # Save complete corrected data
    df.to_csv('non_active_participants_COMPLETE.csv', index=False)
    print(f"\n💾 Saved complete data: non_active_participants_COMPLETE.csv")
    
    # Show summary stats
    print(f"\n📈 DATA COMPLETENESS CHECK:")
    for col in ['useful', 'intent_to_follow']:
        missing = df[col].isna().sum()
        print(f"• {col}: {len(df) - missing}/{len(df)} complete ({missing} missing)")
    
    return df

if __name__ == "__main__":
    complete_data = main() 