import json
import os
import pandas as pd
from collections import defaultdict, Counter

def load_condition_mappings():
    """Load condition mappings from exp_id_map files."""
    condition_mappings = {}
    base_path = "bot_chats"
    
    for round_name in ["round_1", "round_2", "round_3"]:
        exp_id_path = os.path.join(base_path, round_name, "exp_id_map.json")
        if os.path.exists(exp_id_path):
            with open(exp_id_path, 'r', encoding='utf-8') as f:
                exp_id_data = json.load(f)
                for phone, (prolific_id, condition) in exp_id_data.items():
                    condition_mappings[phone] = condition
        else:
            print(f"Warning: {exp_id_path} not found")
    
    return condition_mappings

def load_evaluated_data_with_conditions():
    """Load evaluated conversation data and map to conditions."""
    data = {}
    base_path = "evaluated_bot_chats"
    condition_mappings = load_condition_mappings()
    
    for round_name in ["round_1", "round_2", "round_3"]:
        round_path = os.path.join(base_path, round_name, "message_logs.json")
        if os.path.exists(round_path):
            with open(round_path, 'r', encoding='utf-8') as f:
                round_data = json.load(f)
                data[round_name] = round_data
        else:
            print(f"Warning: {round_path} not found")
    
    return data, condition_mappings

def map_condition_to_name(condition_code):
    """Map condition code to readable name."""
    if condition_code == 1:
        return "Empathetic"
    elif condition_code == 0:
        return "Non-Empathetic"
    else:
        return "Unknown"

def extract_scores_by_dimension_and_condition(data, condition_mappings):
    """Extract scores organized by dimension, session type, and condition."""
    dimensions = ["emotional_reactions", "explorations", "interpretations", "empathy"]
    session_types = ["session_1", "current_session"]  # Initial vs Maintenance sessions
    conditions = ["Empathetic", "Non-Empathetic"]  # Only have these two in the data
    
    # Structure: {dimension: {condition: {session_type: [scores]}}}
    scores_by_dimension_condition = {
        dim: {
            cond: {session: [] for session in session_types} 
            for cond in conditions
        } 
        for dim in dimensions
    }
    
    # Track participants per dimension and condition
    participants_per_dimension_condition = {
        dim: {cond: set() for cond in conditions} 
        for dim in dimensions
    }
    
    for round_name, round_data in data.items():
        for participant, participant_data in round_data.items():
            if participant == "round":  # Skip metadata
                continue
                
            # Get condition for this participant
            condition_code = condition_mappings.get(participant)
            if condition_code is None:
                print(f"Warning: No condition found for participant {participant}")
                continue
                
            condition_name = map_condition_to_name(condition_code)
            if condition_name == "Unknown":
                continue
                
            for dimension in dimensions:
                # Check for scores in both session types
                for session_type in session_types:
                    score_key = f"{session_type}_score_{dimension}"
                    if score_key in participant_data:
                        score = participant_data[score_key]
                        scores_by_dimension_condition[dimension][condition_name][session_type].append(score)
                        participants_per_dimension_condition[dimension][condition_name].add(participant)
    
    return scores_by_dimension_condition, participants_per_dimension_condition

def calculate_statistics(scores):
    """Calculate average and rating distribution for a list of scores."""
    if not scores:
        return None, {}
    
    avg = sum(scores) / len(scores)
    rating_counts = Counter(scores)
    total = len(scores)
    
    # Convert to percentages
    rating_percentages = {}
    for rating in [0, 1, 2]:  # 0-2 scale
        count = rating_counts.get(rating, 0)
        percentage = (count / total * 100) if total > 0 else 0
        rating_percentages[rating] = f"{percentage:.0f}%"
    
    return round(avg, 2), rating_percentages

def create_combined_table(scores_by_dimension_condition, participants_per_dimension_condition):
    """Create a table combining 4 dimensions with 3 conditions (E, NE, Normal)."""
    dimensions = ["emotional_reactions", "explorations", "interpretations", "empathy"]
    conditions = ["Empathetic", "Non-Empathetic"]  # We only have data for these two
    
    # Create table data
    table_data = []
    
    # Header row - create sub-columns for each dimension
    header = [""]
    for dim in dimensions:
        dim_title = dim.replace("_", " ").title()
        for cond in conditions:
            header.append(f"{dim_title} ({cond})")
        # Add placeholder for Normal condition (no data available)
        header.append(f"{dim_title} (Normal)")
    table_data.append(header)
    
    # Number of participants row
    participant_row = ["# Participants"]
    for dim in dimensions:
        for cond in conditions:
            count = len(participants_per_dimension_condition[dim][cond])
            participant_row.append(str(count))
        participant_row.append("0")  # No Normal condition data
    table_data.append(participant_row)
    
    # Initial Session Average
    initial_avg_row = ["Initial Session Avg"]
    for dim in dimensions:
        for cond in conditions:
            scores = scores_by_dimension_condition[dim][cond]["session_1"]
            avg, _ = calculate_statistics(scores)
            initial_avg_row.append(str(avg) if avg is not None else "N/A")
        initial_avg_row.append("N/A")  # No Normal condition data
    table_data.append(initial_avg_row)
    
    # Initial Session Counts/Distribution
    initial_dist_row = ["Initial Session Cts"]
    for dim in dimensions:
        for cond in conditions:
            scores = scores_by_dimension_condition[dim][cond]["session_1"]
            _, rating_dist = calculate_statistics(scores)
            if rating_dist:
                # Find the most common rating
                max_rating = max(rating_dist, key=lambda x: int(rating_dist[x].rstrip('%')))
                max_percentage = rating_dist[max_rating]
                dist_text = f"Rating = {max_rating}: {max_percentage}"
                initial_dist_row.append(dist_text)
            else:
                initial_dist_row.append("N/A")
        initial_dist_row.append("N/A")  # No Normal condition data
    table_data.append(initial_dist_row)
    
    # Maintenance Session Average
    maint_avg_row = ["Maint. Session Avg"]
    for dim in dimensions:
        for cond in conditions:
            scores = scores_by_dimension_condition[dim][cond]["current_session"]
            avg, _ = calculate_statistics(scores)
            maint_avg_row.append(str(avg) if avg is not None else "N/A")
        maint_avg_row.append("N/A")  # No Normal condition data
    table_data.append(maint_avg_row)
    
    # Maintenance Session Counts/Distribution
    maint_dist_row = ["Maint. Session Cts"]
    for dim in dimensions:
        for cond in conditions:
            scores = scores_by_dimension_condition[dim][cond]["current_session"]
            _, rating_dist = calculate_statistics(scores)
            if rating_dist:
                # Show top ratings (similar to original table format)
                sorted_ratings = sorted(rating_dist.items(), 
                                      key=lambda x: int(x[1].rstrip('%')), 
                                      reverse=True)
                dist_lines = []
                for rating, percentage in sorted_ratings[:2]:  # Show top 2
                    if int(percentage.rstrip('%')) > 0:
                        dist_lines.append(f"Rating = {rating}: {percentage}")
                dist_text = " / ".join(dist_lines) if dist_lines else "N/A"
                maint_dist_row.append(dist_text)
            else:
                maint_dist_row.append("N/A")
        maint_dist_row.append("N/A")  # No Normal condition data
    table_data.append(maint_dist_row)
    
    return table_data

def print_detailed_statistics_by_condition(scores_by_dimension_condition):
    """Print detailed statistics for each dimension and condition."""
    print("\n" + "="*100)
    print("DETAILED STATISTICS BY DIMENSION AND CONDITION")
    print("="*100)
    
    dimensions = ["emotional_reactions", "explorations", "interpretations", "empathy"]
    conditions = ["Empathetic", "Non-Empathetic"]
    
    for dim in dimensions:
        print(f"\n📊 {dim.replace('_', ' ').title()}")
        print("-" * 70)
        
        for cond in conditions:
            print(f"\n  🏷️  {cond} Condition:")
            
            for session_type in ["session_1", "current_session"]:
                session_label = "Initial Session" if session_type == "session_1" else "Maintenance Session"
                scores = scores_by_dimension_condition[dim][cond][session_type]
                
                if scores:
                    avg, rating_dist = calculate_statistics(scores)
                    print(f"    {session_label}:")
                    print(f"      Average: {avg}")
                    print(f"      Total responses: {len(scores)}")
                    print(f"      Distribution:")
                    for rating in [0, 1, 2]:
                        count = scores.count(rating)
                        percentage = rating_dist[rating]
                        print(f"        Rating {rating}: {count} responses ({percentage})")
                else:
                    print(f"    {session_label}: No data available")

def create_formatted_table_display(table_data):
    """Create a nicely formatted table for display."""
    print("\n" + "="*180)
    print("4 EMPATHY DIMENSIONS × CONDITIONS ANALYSIS TABLE")
    print("="*180)
    print()
    print("Based on LLM Judge Evaluation (0-2 scale: 0=not at all, 1=somewhat, 2=strongly present)")
    print("Note: Normal condition data not available in current dataset")
    print()
    
    # Print header
    header = table_data[0]
    print(f"{header[0]:<20}", end="")
    for col in header[1:]:
        print(f"{col:<25}", end="")
    print()
    print("-" * 180)
    
    # Print data rows
    for row in table_data[1:]:
        print(f"{row[0]:<20}", end="")
        for cell in row[1:]:
            # Truncate long cell content for display
            cell_str = str(cell)
            if len(cell_str) > 23:
                cell_str = cell_str[:20] + "..."
            print(f"{cell_str:<25}", end="")
        print()
    
    print()
    print("="*180)

def main():
    print("🔍 Loading evaluated conversation data with conditions...")
    data, condition_mappings = load_evaluated_data_with_conditions()
    
    if not data:
        print("❌ No data found. Make sure the evaluated_bot_chats directory exists and contains data.")
        return
    
    print(f"✅ Loaded data from {len(data)} rounds")
    print(f"✅ Found condition mappings for {len(condition_mappings)} participants")
    
    # Show condition distribution
    condition_counts = Counter(condition_mappings.values())
    print(f"   - Empathetic (condition 1): {condition_counts.get(1, 0)} participants")
    print(f"   - Non-Empathetic (condition 0): {condition_counts.get(0, 0)} participants")
    
    print("\n🔄 Extracting scores by dimension and condition...")
    scores_by_dimension_condition, participants_per_dimension_condition = extract_scores_by_dimension_and_condition(data, condition_mappings)
    
    # Create and display the combined table
    table_data = create_combined_table(scores_by_dimension_condition, participants_per_dimension_condition)
    create_formatted_table_display(table_data)
    
    # Print detailed statistics
    print_detailed_statistics_by_condition(scores_by_dimension_condition)
    
    # Save table to CSV for further use
    df = pd.DataFrame(table_data[1:], columns=table_data[0])
    df.to_csv("empathy_dimensions_by_condition_analysis.csv", index=False)
    print(f"\n✅ Table saved to 'empathy_dimensions_by_condition_analysis.csv'")

if __name__ == "__main__":
    main() 