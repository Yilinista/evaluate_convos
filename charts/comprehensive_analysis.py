#!/usr/bin/env python3
"""
Comprehensive Empathy Analysis for Physical Activity Chatbot
Analyzes 4 empathy dimensions: emotional_reactions, explorations, interpretations, empathy
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from collections import defaultdict
import warnings
from scipy import stats
warnings.filterwarnings('ignore')

# Set style
plt.style.use('default')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)

def load_evaluation_data():
    """Load and process empathy evaluation data from all rounds"""
    all_records = []
    
    for round_num in [1, 2, 3]:
        round_name = f"round_{round_num}"
        data_file = Path(f"evaluated_bot_chats/{round_name}/message_logs.json")
        
        if not data_file.exists():
            print(f"File not found: {data_file}")
            continue
            
        with open(data_file, 'r') as f:
            data = json.load(f)
        
        for participant, participant_data in data.items():
            # Skip if participant_data is not a dictionary or is "round" metadata
            if not isinstance(participant_data, dict) or participant == "round":
                continue
                
            # Get session names (exclude score fields)
            session_names = [key for key in participant_data.keys() 
                            if not any(key.endswith(f'_score_{metric}') 
                                     for metric in ['empathy', 'emotional_reactions', 'explorations', 'interpretations'])]
            
            for session_name in session_names:
                empathy_field = f"{session_name}_score_empathy"
                
                if empathy_field in participant_data:
                    # Calculate conversation length
                    convo_length = len(participant_data.get(session_name, []))
                    
                    record = {
                        "round": round_name,
                        "round_num": round_num,
                        "participant": participant,
                        "session": session_name,
                        "emotional_reactions": participant_data.get(f"{session_name}_score_emotional_reactions", 0),
                        "explorations": participant_data.get(f"{session_name}_score_explorations", 0),
                        "interpretations": participant_data.get(f"{session_name}_score_interpretations", 0),
                        "empathy": participant_data.get(empathy_field, 0),
                        "conversation_length": convo_length
                    }
                    all_records.append(record)
    
    return pd.DataFrame(all_records)

def analyze_score_distributions(df, empathy_cols):
    """Analyze score distributions across all dimensions"""
    print("=" * 50)
    print("1. SCORE DISTRIBUTIONS")
    print("=" * 50)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for i, col in enumerate(empathy_cols):
        ax = axes[i]
        df[col].value_counts().sort_index().plot(kind='bar', ax=ax, color=sns.color_palette()[i])
        ax.set_title(f'{col.replace("_", " ").title()} Distribution')
        ax.set_xlabel('Score')
        ax.set_ylabel('Frequency')
        ax.tick_params(axis='x', rotation=0)

    plt.tight_layout()
    plt.savefig('score_distributions.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Summary statistics
    print("\nSummary Statistics:")
    print(df[empathy_cols].describe())
    
    print("\nScore Mode Analysis:")
    for col in empathy_cols:
        mode_score = df[col].mode().iloc[0]
        mode_pct = (df[col] == mode_score).mean() * 100
        print(f"{col.replace('_', ' ').title()}: Most common score is {mode_score} ({mode_pct:.1f}% of conversations)")

def analyze_correlations(df, empathy_cols):
    """Analyze correlations between empathy dimensions"""
    print("\n" + "=" * 50)
    print("2. CORRELATION ANALYSIS")
    print("=" * 50)
    
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[empathy_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, linewidths=0.5)
    plt.title('Correlation Matrix of Empathy Dimensions')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("Strongest correlations:")
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    corr_pairs = correlation_matrix.where(~mask).stack().sort_values(ascending=False)
    print(corr_pairs.head(6))
    
    # Statistical significance tests
    print("\nCorrelation significance tests:")
    for i, col1 in enumerate(empathy_cols):
        for col2 in empathy_cols[i+1:]:
            corr, p_value = stats.pearsonr(df[col1], df[col2])
            sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
            print(f"{col1} vs {col2}: r={corr:.3f}, p={p_value:.4f} {sig}")

def analyze_participant_journeys(df, empathy_cols):
    """Track participants across rounds"""
    print("\n" + "=" * 50)
    print("3. PARTICIPANT JOURNEY ANALYSIS")
    print("=" * 50)
    
    participant_rounds = df.groupby('participant')['round_num'].unique().apply(list)
    multi_round_participants = participant_rounds[participant_rounds.apply(len) > 1]

    print(f"Participants in multiple rounds: {len(multi_round_participants)}")
    print(f"Single-round participants: {len(participant_rounds) - len(multi_round_participants)}")

    # Retention analysis
    round_participation = df.groupby('round_num')['participant'].nunique()
    print("\nParticipation by round:")
    for round_num, count in round_participation.items():
        print(f"Round {round_num}: {count} participants")

    # Participant journey visualization
    journey_df = df.groupby(['participant', 'round_num'])[empathy_cols].mean().reset_index()

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()

    for i, col in enumerate(empathy_cols):
        ax = axes[i]
        
        # Plot individual participant journeys
        for participant in multi_round_participants.index:
            participant_data = journey_df[journey_df['participant'] == participant]
            if len(participant_data) > 1:
                ax.plot(participant_data['round_num'], participant_data[col], 
                       'o-', alpha=0.3, color='gray', linewidth=0.5)
        
        # Plot average trend
        avg_by_round = journey_df.groupby('round_num')[col].mean()
        ax.plot(avg_by_round.index, avg_by_round.values, 'o-', 
               color=sns.color_palette()[i], linewidth=3, markersize=8, label='Average')
        
        ax.set_title(f'{col.replace("_", " ").title()} Evolution')
        ax.set_xlabel('Round')
        ax.set_ylabel('Score')
        ax.set_ylim(0, 2)
        ax.grid(True, alpha=0.3)
        ax.legend()

    plt.tight_layout()
    plt.savefig('participant_journeys.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return multi_round_participants

def analyze_session_performance(df, empathy_cols):
    """Analyze performance by session type"""
    print("\n" + "=" * 50)
    print("4. SESSION-LEVEL ANALYSIS")
    print("=" * 50)
    
    session_analysis = df.groupby('session')[empathy_cols].agg(['mean', 'std', 'count']).round(3)
    print("Performance by Session Type:")
    print(session_analysis)

    # Visualize session performance
    session_means = df.groupby('session')[empathy_cols].mean()

    plt.figure(figsize=(12, 6))
    session_means.plot(kind='bar', width=0.8)
    plt.title('Average Scores by Session Type')
    plt.xlabel('Session')
    plt.ylabel('Average Score')
    plt.legend(title='Empathy Dimension', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('session_performance.png', dpi=300, bbox_inches='tight')
    plt.show()

def analyze_conversation_length_impact(df, empathy_cols):
    """Analyze relationship between conversation length and empathy scores"""
    print("\n" + "=" * 50)
    print("5. CONVERSATION LENGTH IMPACT")
    print("=" * 50)
    
    print("Conversation Length Statistics:")
    print(df['conversation_length'].describe())

    # Correlation with conversation length
    length_correlations = df[empathy_cols + ['conversation_length']].corr()['conversation_length'].drop('conversation_length')
    print("\nCorrelation with Conversation Length:")
    print(length_correlations.sort_values(ascending=False))

    # Scatter plots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for i, col in enumerate(empathy_cols):
        ax = axes[i]
        ax.scatter(df['conversation_length'], df[col], alpha=0.6, color=sns.color_palette()[i])
        
        # Add trend line
        z = np.polyfit(df['conversation_length'], df[col], 1)
        p = np.poly1d(z)
        ax.plot(df['conversation_length'], p(df['conversation_length']), "r--", alpha=0.8)
        
        ax.set_xlabel('Conversation Length (messages)')
        ax.set_ylabel(f'{col.replace("_", " ").title()} Score')
        ax.set_title(f'{col.replace("_", " ").title()} vs Conversation Length')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('conversation_length_impact.png', dpi=300, bbox_inches='tight')
    plt.show()

def analyze_improvement_patterns(df, empathy_cols, multi_round_participants):
    """Calculate improvement for multi-round participants"""
    print("\n" + "=" * 50)
    print("6. PERFORMANCE IMPROVEMENT ANALYSIS")
    print("=" * 50)
    
    improvement_data = []

    for participant in multi_round_participants.index:
        participant_data = df[df['participant'] == participant].groupby('round_num')[empathy_cols].mean()
        
        if len(participant_data) >= 2:
            # Calculate change from first to last round
            first_round = participant_data.iloc[0]
            last_round = participant_data.iloc[-1]
            
            improvement = {
                'participant': participant,
                'rounds_participated': len(participant_data),
                'first_round': participant_data.index[0],
                'last_round': participant_data.index[-1]
            }
            
            for col in empathy_cols:
                improvement[f'{col}_change'] = last_round[col] - first_round[col]
                improvement[f'{col}_first'] = first_round[col]
                improvement[f'{col}_last'] = last_round[col]
            
            improvement_data.append(improvement)

    improvement_df = pd.DataFrame(improvement_data)

    if len(improvement_df) > 0:
        # Visualize improvements
        change_cols = [f'{col}_change' for col in empathy_cols]
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()
        
        for i, col in enumerate(change_cols):
            ax = axes[i]
            
            # Histogram of changes
            ax.hist(improvement_df[col], bins=10, alpha=0.7, color=sns.color_palette()[i])
            ax.axvline(x=0, color='red', linestyle='--', alpha=0.7)
            ax.axvline(x=improvement_df[col].mean(), color='green', linestyle='-', alpha=0.7, 
                      label=f'Mean: {improvement_df[col].mean():.2f}')
            
            ax.set_xlabel('Score Change')
            ax.set_ylabel('Frequency')
            ax.set_title(f'{col.replace("_change", "").replace("_", " ").title()} Change Distribution')
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('improvement_patterns.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Summary statistics
        print(f"Participants with improvement data: {len(improvement_df)}")
        print("\nAverage changes:")
        for col in empathy_cols:
            change_col = f'{col}_change'
            avg_change = improvement_df[change_col].mean()
            improved_count = (improvement_df[change_col] > 0).sum()
            total_count = len(improvement_df)
            print(f"{col.replace('_', ' ').title()}: {avg_change:+.3f} ({improved_count}/{total_count} improved)")
    else:
        print("No multi-round participants found for improvement analysis.")
    
    return improvement_df

def bot_performance_summary(df, empathy_cols):
    """Overall bot performance summary"""
    print("\n" + "=" * 50)
    print("7. BOT PERFORMANCE INSIGHTS")
    print("=" * 50)
    
    print(f"Total conversations analyzed: {len(df)}")
    print(f"Total participants: {df['participant'].nunique()}")
    print(f"Average conversation length: {df['conversation_length'].mean():.1f} messages")

    print("\nOverall Average Scores (0-2 scale):")
    for col in empathy_cols:
        avg_score = df[col].mean()
        max_score = df[col].max()
        pct_max = (df[col] == 2).mean() * 100
        print(f"{col.replace('_', ' ').title()}: {avg_score:.3f} (Max: {max_score}, {pct_max:.1f}% scored 2)")

    # Performance by round
    print("\nPerformance by Round:")
    round_performance = df.groupby('round')[empathy_cols].mean()
    print(round_performance.round(3))

    # Best and worst performers
    df['total_score'] = df[empathy_cols].sum(axis=1)
    df['avg_score'] = df[empathy_cols].mean(axis=1)

    print("\nTop 5 Highest Scoring Conversations:")
    top_conversations = df.nlargest(5, 'total_score')[['participant', 'round', 'session', 'total_score'] + empathy_cols]
    print(top_conversations)

    print("\nTop 5 Lowest Scoring Conversations:")
    bottom_conversations = df.nsmallest(5, 'total_score')[['participant', 'round', 'session', 'total_score'] + empathy_cols]
    print(bottom_conversations)

def statistical_tests(df, empathy_cols):
    """Perform statistical tests"""
    print("\n" + "=" * 50)
    print("8. STATISTICAL TESTS")
    print("=" * 50)
    
    # Test for differences between rounds
    print("Kruskal-Wallis test for differences between rounds:")
    for col in empathy_cols:
        groups = [df[df['round'] == f'round_{i}'][col] for i in [1, 2, 3]]
        groups = [g for g in groups if len(g) > 0]
        
        if len(groups) >= 2:
            statistic, p_value = stats.kruskal(*groups)
            sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
            print(f"{col.replace('_', ' ').title()}: H={statistic:.3f}, p={p_value:.4f} {sig}")

    # Test for differences between session types
    print("\nKruskal-Wallis test for differences between session types:")
    session_types = df['session'].unique()

    if len(session_types) > 1:
        for col in empathy_cols:
            groups = [df[df['session'] == session][col] for session in session_types]
            groups = [g for g in groups if len(g) > 0]
            
            if len(groups) >= 2:
                statistic, p_value = stats.kruskal(*groups)
                sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
                print(f"{col.replace('_', ' ').title()}: H={statistic:.3f}, p={p_value:.4f} {sig}")

def key_findings_summary(df, empathy_cols, improvement_df=None):
    """Summarize key findings"""
    print("\n" + "=" * 80)
    print("KEY FINDINGS SUMMARY")
    print("=" * 80)
    
    print("\n🎯 SCORE DISTRIBUTIONS:")
    for col in empathy_cols:
        mode_score = df[col].mode().iloc[0]
        mode_pct = (df[col] == mode_score).mean() * 100
        avg_score = df[col].mean()
        print(f"   {col.replace('_', ' ').title()}: Avg={avg_score:.2f}, Mode={mode_score} ({mode_pct:.1f}%)")

    print("\n🔗 STRONGEST CORRELATIONS:")
    corr_matrix = df[empathy_cols].corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    corr_pairs = corr_matrix.where(~mask).stack().sort_values(ascending=False)
    for pair, corr in corr_pairs.head(3).items():
        print(f"   {pair[0]} & {pair[1]}: r = {corr:.3f}")

    print("\n👥 PARTICIPANT RETENTION:")
    retention_stats = df.groupby('participant')['round_num'].nunique().value_counts().sort_index()
    for rounds, count in retention_stats.items():
        print(f"   {count} participants in {rounds} round(s)")

    print("\n💬 SESSION PERFORMANCE:")
    session_performance = df.groupby('session')['avg_score'].mean().sort_values(ascending=False)
    if len(session_performance) > 0:
        best_session = session_performance.index[0]
        worst_session = session_performance.index[-1]
        print(f"   Best: {best_session} (avg: {session_performance[best_session]:.3f})")
        print(f"   Worst: {worst_session} (avg: {session_performance[worst_session]:.3f})")

    print("\n📏 CONVERSATION LENGTH IMPACT:")
    length_corr = df[['conversation_length'] + empathy_cols].corr()['conversation_length'].drop('conversation_length')
    strongest_length_corr = length_corr.abs().idxmax()
    print(f"   Strongest correlation: {strongest_length_corr} (r = {length_corr[strongest_length_corr]:.3f})")

    if improvement_df is not None and len(improvement_df) > 0:
        print("\n📈 IMPROVEMENT PATTERNS:")
        for col in empathy_cols:
            change_col = f'{col}_change'
            avg_change = improvement_df[change_col].mean()
            improved_pct = (improvement_df[change_col] > 0).mean() * 100
            print(f"   {col.replace('_', ' ').title()}: {improved_pct:.1f}% improved (avg: {avg_change:+.3f})")

def main():
    """Main analysis function"""
    print("🤖 COMPREHENSIVE EMPATHY ANALYSIS")
    print("Physical Activity Chatbot Evaluation")
    print("=" * 80)
    
    # Load data
    df = load_evaluation_data()
    empathy_cols = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    if len(df) == 0:
        print("❌ No data found. Please check that evaluated data files exist.")
        return
    
    print(f"✅ Loaded {len(df)} conversation records")
    print(f"✅ {df['participant'].nunique()} unique participants")
    
    # Run analyses
    analyze_score_distributions(df, empathy_cols)
    analyze_correlations(df, empathy_cols)
    multi_round_participants = analyze_participant_journeys(df, empathy_cols)
    analyze_session_performance(df, empathy_cols)
    analyze_conversation_length_impact(df, empathy_cols)
    improvement_df = analyze_improvement_patterns(df, empathy_cols, multi_round_participants)
    bot_performance_summary(df, empathy_cols)
    statistical_tests(df, empathy_cols)
    key_findings_summary(df, empathy_cols, improvement_df)
    
    print(f"\n✅ Analysis complete! Generated plots saved as PNG files.")
    print("📊 Check the following files:")
    print("   - score_distributions.png")
    print("   - correlation_matrix.png") 
    print("   - participant_journeys.png")
    print("   - session_performance.png")
    print("   - conversation_length_impact.png")
    print("   - improvement_patterns.png")

if __name__ == "__main__":
    main() 