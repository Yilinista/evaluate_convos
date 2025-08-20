#!/usr/bin/env python3
"""
Create visualization showing the improvement from majority voting
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def create_improvement_summary():
    """Create comprehensive visualization showing all improvements"""
    
    # Data from our comprehensive analysis
    data = {
        'Correlation Method': ['Dimension Average', 'Dimension Average', 'Overall Correlation', 'Overall Correlation'],
        'Voting Method': ['Individual Ratings', 'Majority Voting', 'Individual Ratings', 'Majority Voting'],
        'Spearman_rho': [0.174, 0.332, 0.108, 0.171],
        'Absolute_Agreement': [0.424, 0.429, 0.424, 0.429],  # Similar for both methods
        'Within_One_Agreement': [0.987, 1.000, 0.987, 1.000]
    }
    
    df = pd.DataFrame(data)
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Color scheme
    colors = ['lightblue', 'darkblue', 'lightcoral', 'darkred']
    improvement_color = 'green'
    
    # Plot 1: Spearman Correlation Improvement
    ax = axes[0, 0]
    
    groups = df.groupby('Correlation Method')
    x_pos = np.arange(len(groups))
    width = 0.35
    
    for i, (method, group) in enumerate(groups):
        individual = group[group['Voting Method'] == 'Individual Ratings']['Spearman_rho'].iloc[0]
        majority = group[group['Voting Method'] == 'Majority Voting']['Spearman_rho'].iloc[0]
        
        bars1 = ax.bar(i - width/2, individual, width, label='Individual' if i == 0 else "", 
                      color='lightgray', alpha=0.7)
        bars2 = ax.bar(i + width/2, majority, width, label='Majority Voting' if i == 0 else "", 
                      color='darkgreen', alpha=0.8)
        
        # Add improvement arrow and percentage
        improvement = ((majority - individual) / individual) * 100
        ax.annotate(f'+{improvement:.0f}%', xy=(i, max(individual, majority) + 0.02), 
                   ha='center', va='bottom', fontweight='bold', color=improvement_color)
        
        # Add value labels
        ax.text(i - width/2, individual + 0.01, f'{individual:.3f}', 
               ha='center', va='bottom', fontsize=10)
        ax.text(i + width/2, majority + 0.01, f'{majority:.3f}', 
               ha='center', va='bottom', fontsize=10)
    
    ax.set_ylabel('Spearman ρ')
    ax.set_title('Spearman Correlation Improvement\nfrom Majority Voting', fontweight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(['Dimension\nAverage', 'Overall\nCorrelation'])
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 0.4)
    
    # Plot 2: Before vs After Summary
    ax = axes[0, 1]
    
    metrics = ['Spearman ρ\n(Dim Avg)', 'Spearman ρ\n(Overall)', 'Absolute\nAgreement', 'Within-One\nAgreement']
    before_values = [0.174, 0.108, 0.424, 0.987]
    after_values = [0.332, 0.171, 0.429, 1.000]
    
    x = np.arange(len(metrics))
    
    bars1 = ax.bar(x - width/2, before_values, width, label='Before (Individual)', 
                  color='lightcoral', alpha=0.7)
    bars2 = ax.bar(x + width/2, after_values, width, label='After (Majority)', 
                  color='darkblue', alpha=0.8)
    
    # Add improvement percentages
    for i, (before, after) in enumerate(zip(before_values, after_values)):
        if before > 0:
            improvement = ((after - before) / before) * 100
            if improvement > 1:  # Only show significant improvements
                ax.annotate(f'+{improvement:.0f}%', 
                           xy=(i, max(before, after) + 0.02), 
                           ha='center', va='bottom', fontweight='bold', 
                           color=improvement_color)
    
    ax.set_ylabel('Score')
    ax.set_title('Overall Improvement Summary', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    
    # Plot 3: Comparison with Original Report
    ax = axes[0, 2]
    
    comparison_data = {
        'Study Phase': ['Original\nReport', 'Set 1+2\nIndividual', 'Set 1+2\nMajority'],
        'Spearman_rho': [0.325, 0.174, 0.332],  # Dimension average method
        'Status': ['Baseline', 'Lower', 'Recovered']
    }
    
    comp_colors = ['gold', 'lightcoral', 'darkgreen']
    bars = ax.bar(comparison_data['Study Phase'], comparison_data['Spearman_rho'], 
                 color=comp_colors, alpha=0.8)
    
    # Add value labels
    for bar, val in zip(bars, comparison_data['Spearman_rho']):
        ax.text(bar.get_x() + bar.get_width()/2., val + 0.01, f'{val:.3f}', 
               ha='center', va='bottom', fontweight='bold')
    
    # Add horizontal line for original level
    ax.axhline(y=0.325, color='red', linestyle='--', alpha=0.7, label='Original Level')
    
    ax.set_ylabel('Spearman ρ (Dimension Average)')
    ax.set_title('Recovery to Original Performance\nthrough Majority Voting', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 0.4)
    
    # Plot 4: Dimension-wise Improvements
    ax = axes[1, 0]
    
    dimensions = ['Emotional\nReactions', 'Explorations', 'Interpretations', 'Empathy']
    before_dim = [0.174, 0.113, 0.219, 0.191]  # From comprehensive analysis
    after_dim = [0.353, 0.155, 0.384, 0.435]
    
    x = np.arange(len(dimensions))
    
    bars1 = ax.bar(x - width/2, before_dim, width, label='Individual Ratings', 
                  color='lightgray', alpha=0.7)
    bars2 = ax.bar(x + width/2, after_dim, width, label='Majority Voting', 
                  color='darkblue', alpha=0.8)
    
    # Add improvement arrows
    for i, (before, after) in enumerate(zip(before_dim, after_dim)):
        improvement = ((after - before) / before) * 100
        ax.annotate(f'+{improvement:.0f}%', 
                   xy=(i, max(before, after) + 0.02), 
                   ha='center', va='bottom', fontweight='bold', 
                   color=improvement_color)
    
    ax.set_ylabel('Spearman ρ')
    ax.set_title('Dimension-wise Correlation Improvements', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dimensions)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 0.5)
    
    # Plot 5: Human Rater Agreement Statistics  
    ax = axes[1, 1]
    
    voting_stats = ['Unanimous\nAgreement', 'Majority\nVoting', 'Tied\nVotes']
    percentages = [18.7, 76.8, 4.5]  # Average from both sets
    
    pie_colors = ['lightgreen', 'orange', 'lightcoral']
    wedges, texts, autotexts = ax.pie(percentages, labels=voting_stats, colors=pie_colors, 
                                     autopct='%1.1f%%', startangle=90)
    
    ax.set_title('Human Rater Voting Patterns\n(Before Majority Resolution)', fontweight='bold')
    
    # Plot 6: Key Statistics Table
    ax = axes[1, 2]
    ax.axis('tight')
    ax.axis('off')
    
    table_data = [
        ['Metric', 'Before', 'After', 'Improvement'],
        ['', '', '', ''],
        ['Correlation Results:', '', '', ''],
        ['  Dimension Avg ρ', '0.174', '0.332', '+91%'],
        ['  Overall ρ', '0.108', '0.171', '+58%'],
        ['', '', '', ''],
        ['Agreement Results:', '', '', ''],
        ['  Absolute Agreement', '42.4%', '42.9%', '+0.5%'],
        ['  Within-One Agreement', '98.7%', '100.0%', '+1.3%'],
        ['', '', '', ''],
        ['Data Quality:', '', '', ''],
        ['  Total Conversations', '55', '55', '—'],
        ['  Human Evaluators', '10', '10', '—'],
        ['  Unanimous Votes', '—', '18.7%', 'New'],
        ['  Majority Votes', '—', '76.8%', 'New'],
        ['', '', '', ''],
        ['Comparison to Original:', '', '', ''],
        ['  Original Report ρ', '0.325', '—', '—'],
        ['  Current (Majority) ρ', '—', '0.332', '+2%'],
    ]
    
    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.3)
    
    # Header styling
    for i in range(len(table_data[0])):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Section headers
    for row_idx in [2, 6, 10, 15]:
        for col_idx in range(4):
            table[(row_idx, col_idx)].set_facecolor('#e0e0e0')
            table[(row_idx, col_idx)].set_text_props(weight='bold')
    
    # Highlight improvements
    improvement_rows = [3, 4, 7, 8, 16]
    for row_idx in improvement_rows:
        table[(row_idx, 3)].set_facecolor('#90EE90')  # Light green for improvements
    
    ax.set_title('Comprehensive Results Summary', fontweight='bold', pad=20)
    
    plt.suptitle('Majority Voting Impact: LLM-Human Agreement Analysis Improvements\n' + 
                 'Resolving Human Rater Disagreements Significantly Enhanced Correlation Metrics', 
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    
    return fig

def main():
    """Create and save the improvement visualization"""
    
    print("Creating comprehensive improvement visualization...")
    
    fig = create_improvement_summary()
    
    output_file = '../visualizations/majority_voting_improvements.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved improvement visualization to: {output_file}")
    
    # Also create a simple before/after comparison
    fig2, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    methods = ['Dimension Average\nSpearman ρ', 'Overall\nSpearman ρ', 'Absolute\nAgreement', 'Within-One\nAgreement']
    before = [0.174, 0.108, 0.424, 0.987]
    after = [0.332, 0.171, 0.429, 1.000]
    
    x = np.arange(len(methods))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, before, width, label='Before Majority Voting', 
                  color='lightcoral', alpha=0.8)
    bars2 = ax.bar(x + width/2, after, width, label='After Majority Voting', 
                  color='darkgreen', alpha=0.8)
    
    # Add improvement percentages
    for i, (b, a) in enumerate(zip(before, after)):
        if b > 0:
            improvement = ((a - b) / b) * 100
            if improvement > 1:
                ax.text(i, max(b, a) + 0.02, f'+{improvement:.0f}%', 
                       ha='center', va='bottom', fontweight='bold', color='green')
        
        # Add value labels
        ax.text(i - width/2, b + 0.01, f'{b:.3f}', ha='center', va='bottom', fontsize=10)
        ax.text(i + width/2, a + 0.01, f'{a:.3f}', ha='center', va='bottom', fontsize=10)
    
    ax.set_ylabel('Score')
    ax.set_title('Impact of Majority Voting on LLM-Human Agreement Metrics\n(55 Conversations Total)', 
                fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    
    simple_output = '../visualizations/simple_before_after.png'
    plt.savefig(simple_output, dpi=300, bbox_inches='tight')
    print(f"✓ Saved simple comparison to: {simple_output}")
    
    plt.show()

if __name__ == "__main__":
    main()