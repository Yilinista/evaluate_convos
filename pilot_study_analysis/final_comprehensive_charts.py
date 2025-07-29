import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_final_comprehensive_charts():
    """Create final comprehensive charts with ALL data including useful and intent_to_follow"""
    
    # Load the complete corrected data
    df = pd.read_csv('non_active_CORRECTED_FINAL.csv')
    
    print("📊 FINAL COMPREHENSIVE ANALYSIS - ALL METRICS INCLUDED")
    print("=" * 75)
    print(f"Total participants: {len(df)}")
    print("\nConditions: Empathetic vs Non-Empathetic")
    print("\nComplete participant data:")
    display_cols = ['prolific_id', 'condition', 'satisfaction', 'enjoyment', 'useful', 
                   'intent_to_follow', 'confidence', 'naturalistic']
    print(df[display_cols].to_string(index=False))
    
    # Set up plotting style
    plt.style.use('default')
    sns.set_palette("Set2")
    
    # Color mapping for the conditions
    color_map = {'Empathetic': '#7fbf7f', 'Non-Empathetic': '#ff7f7f'}
    
    # Create comprehensive chart with ALL metrics (now including useful and intent)
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle('FINAL COMPREHENSIVE Analysis: Non-Physically Active Participants (n=4)\nALL Metrics Including Usefulness & Intent to Follow', 
                 fontsize=16, fontweight='bold')
    
    # All available metrics to visualize
    perception_metrics = [
        ('satisfaction', 'Overall Satisfaction'),
        ('enjoyment', 'Enjoyment'),
        ('useful', 'Usefulness'),
        ('intent_to_follow', 'Intent to Follow'),
        ('confidence', 'Confidence'),
        ('naturalistic', 'Naturalistic Responses'),
        ('ease_of_use', 'Ease of Use')
    ]
    
    participant_labels = [f"P{i+1}\n({row['condition']})" for i, (_, row) in enumerate(df.iterrows())]
    colors = [color_map[cond] for cond in df['condition']]
    
    # Create individual metric charts
    for idx, (metric, title) in enumerate(perception_metrics):
        row = idx // 4
        col = idx % 4
        ax = axes[row, col]
        
        # Create bar chart
        values = df[metric]
        bars = ax.bar(participant_labels, values, color=colors, alpha=0.7, edgecolor='black')
        
        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.set_ylabel('Score')
        ax.set_ylim(0, 6)
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                   f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        # Rotate x-axis labels for readability
        ax.tick_params(axis='x', rotation=45)
    
    # Add condition comparison chart in the last subplot
    ax_comparison = axes[1, 3]
    
    # Condition comparison for key metrics
    key_metrics = ['satisfaction', 'enjoyment', 'useful', 'intent_to_follow', 'confidence', 'naturalistic', 'ease_of_use']
    condition_means = df.groupby('condition')[key_metrics].mean()
    
    x = np.arange(len(key_metrics))
    width = 0.35
    
    if 'Empathetic' in condition_means.index:
        emp_means = condition_means.loc['Empathetic'].values
        bars1 = ax_comparison.bar(x - width/2, emp_means, width, label='Empathetic', color='#7fbf7f', alpha=0.7)
        
        # Add value labels
        for bar, val in zip(bars1, emp_means):
            ax_comparison.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                             f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=8)
    
    if 'Non-Empathetic' in condition_means.index:
        ne_means = condition_means.loc['Non-Empathetic'].values
        bars2 = ax_comparison.bar(x + width/2, ne_means, width, label='Non-Empathetic', color='#ff7f7f', alpha=0.7)
        
        # Add value labels
        for bar, val in zip(bars2, ne_means):
            ax_comparison.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                             f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=8)
    
    ax_comparison.set_title('Condition Comparison', fontweight='bold')
    ax_comparison.set_ylabel('Average Score')
    ax_comparison.set_ylim(0, 6)
    ax_comparison.set_xticks(x)
    ax_comparison.set_xticklabels(['Satisfaction', 'Enjoyment', 'Useful', 'Intent', 'Confidence', 'Naturalistic', 'Ease of Use'], rotation=45)
    ax_comparison.legend()
    ax_comparison.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('FINAL_comprehensive_charts.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

def create_detailed_comparison():
    """Create detailed comparison charts"""
    
    df = pd.read_csv('non_active_CORRECTED_FINAL.csv')
    
    # Create detailed comparison
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Detailed Condition Comparison: Empathetic vs Non-Empathetic\n(Non-Physically Active Participants)', 
                 fontsize=16, fontweight='bold')
    
    # 1. All Perception Metrics Side-by-Side
    ax1 = axes[0, 0]
    metrics = ['satisfaction', 'enjoyment', 'useful', 'intent_to_follow', 'confidence', 'naturalistic', 'ease_of_use']
    condition_means = df.groupby('condition')[metrics].mean()
    
    x = np.arange(len(metrics))
    width = 0.35
    
    emp_means = condition_means.loc['Empathetic'].values if 'Empathetic' in condition_means.index else []
    ne_means = condition_means.loc['Non-Empathetic'].values if 'Non-Empathetic' in condition_means.index else []
    
    if len(emp_means) > 0:
        bars1 = ax1.bar(x - width/2, emp_means, width, label='Empathetic', color='#7fbf7f', alpha=0.7)
        for bar, val in zip(bars1, emp_means):
            ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                    f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    if len(ne_means) > 0:
        bars2 = ax1.bar(x + width/2, ne_means, width, label='Non-Empathetic', color='#ff7f7f', alpha=0.7)
        for bar, val in zip(bars2, ne_means):
            ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                    f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    ax1.set_title('All Perception Metrics Comparison', fontweight='bold')
    ax1.set_ylabel('Average Score')
    ax1.set_ylim(0, 6)
    ax1.set_xticks(x)
    ax1.set_xticklabels(['Satisfaction', 'Enjoyment', 'Useful', 'Intent', 'Confidence', 'Naturalistic', 'Ease of Use'], rotation=45)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. Individual Participant Profiles
    ax2 = axes[0, 1]
    key_metrics = ['satisfaction', 'enjoyment', 'useful', 'intent_to_follow', 'confidence', 'naturalistic', 'ease_of_use']
    
    for i, (_, participant) in enumerate(df.iterrows()):
        values = [participant[metric] for metric in key_metrics]
        color = '#7fbf7f' if participant['condition'] == 'Empathetic' else '#ff7f7f'
        ax2.plot(key_metrics, values, 'o-', label=f"P{i+1} ({participant['condition']})", 
                color=color, linewidth=2, markersize=8, alpha=0.8)
    
    ax2.set_title('Individual Participant Profiles', fontweight='bold')
    ax2.set_ylabel('Score')
    ax2.set_ylim(0, 6)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # 3. Key Insights Box
    ax3 = axes[1, 0]
    ax3.axis('off')
    
    # Calculate key insights
    emp_subset = df[df['condition'] == 'Empathetic']
    ne_subset = df[df['condition'] == 'Non-Empathetic']
    
    insights_text = "🎯 KEY INSIGHTS\n\n"
    insights_text += f"Empathetic Condition (n={len(emp_subset)}): \n"
    insights_text += f"  • Satisfaction: {emp_subset['satisfaction'].mean():.1f}\n"
    insights_text += f"  • Useful: {emp_subset['useful'].mean():.1f}\n"
    insights_text += f"  • Intent: {emp_subset['intent_to_follow'].mean():.1f}\n\n"
    
    insights_text += f"Non-Empathetic Condition (n={len(ne_subset)}): \n"
    insights_text += f"  • Satisfaction: {ne_subset['satisfaction'].mean():.1f}\n"
    insights_text += f"  • Useful: {ne_subset['useful'].mean():.1f}\n"
    insights_text += f"  • Intent: {ne_subset['intent_to_follow'].mean():.1f}\n\n"
    
    # Identify winners
    insights_text += "🏆 WINNERS:\n"
    if emp_subset['satisfaction'].mean() > ne_subset['satisfaction'].mean():
        insights_text += "  • Satisfaction: Empathetic\n"
    else:
        insights_text += "  • Satisfaction: Non-Empathetic\n"
        
    if emp_subset['useful'].mean() > ne_subset['useful'].mean():
        insights_text += "  • Usefulness: Empathetic\n"
    else:
        insights_text += "  • Usefulness: Non-Empathetic\n"
        
    if emp_subset['intent_to_follow'].mean() > ne_subset['intent_to_follow'].mean():
        insights_text += "  • Intent to Follow: Empathetic\n"
    else:
        insights_text += "  • Intent to Follow: Non-Empathetic\n"
    
    ax3.text(0.1, 0.9, insights_text, transform=ax3.transAxes, fontsize=11,
            verticalalignment='top', fontfamily='monospace')
    
    # 4. Summary Statistics Table
    ax4 = axes[1, 1]
    
    # Create summary statistics
    summary_stats = df.groupby('condition').agg({
        'satisfaction': ['mean', 'std'],
        'enjoyment': ['mean', 'std'],
        'useful': ['mean', 'std'],
        'intent_to_follow': ['mean', 'std'],
        'confidence': ['mean', 'std'],
        'naturalistic': ['mean', 'std'],
        'ease_of_use': ['mean', 'std']
    }).round(2)
    
    # Convert to text representation
    ax4.axis('off')
    table_text = "📊 SUMMARY STATISTICS\n\n"
    
    for condition in ['Empathetic', 'Non-Empathetic']:
        if condition in summary_stats.index:
            table_text += f"{condition}:\n"
            for metric in ['satisfaction', 'enjoyment', 'useful', 'intent_to_follow', 'confidence', 'naturalistic', 'ease_of_use']:
                mean_val = summary_stats.loc[condition, (metric, 'mean')]
                std_val = summary_stats.loc[condition, (metric, 'std')]
                table_text += f"  {metric}: {mean_val} ± {std_val}\n"
            table_text += "\n"
    
    ax4.text(0.1, 0.9, table_text, transform=ax4.transAxes, fontsize=10,
            verticalalignment='top', fontfamily='monospace')
    
    plt.tight_layout()
    plt.savefig('FINAL_detailed_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n📈 FINAL COMPREHENSIVE CONDITION BREAKDOWN:")
    print(df.groupby('condition')[['satisfaction', 'enjoyment', 'useful', 'intent_to_follow', 'confidence', 'naturalistic', 'ease_of_use']].agg(['mean', 'count']).round(2))

if __name__ == "__main__":
    # Run final comprehensive analysis
    data = create_final_comprehensive_charts()
    create_detailed_comparison()
    
    print("\n💾 FINAL COMPREHENSIVE Charts saved:")
    print("• FINAL_comprehensive_charts.png (8 panels with ALL metrics)")
    print("• FINAL_detailed_comparison.png (detailed condition analysis)") 