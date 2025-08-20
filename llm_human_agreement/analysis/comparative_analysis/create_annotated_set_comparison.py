#!/usr/bin/env python3
"""
Create annotated version of the Set 1 vs Set 2 comparison figure
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def create_annotated_set_comparison():
    """Create the 6-panel set comparison figure with descriptions"""
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # ========== ROW 1: Main Metrics Comparison ==========
    
    # Plot 1: Absolute Agreement (Top Left)
    ax = axes[0, 0]
    categories = ['Set 1\nIndividual', 'Set 1\nMajority', 'Set 2\nIndividual', 'Set 2\nMajority']
    values = [0.42, 0.375, 0.48, 0.546]
    colors = ['lightblue', 'darkblue', 'lightcoral', 'darkred']
    
    bars = ax.bar(categories, values, color=colors, alpha=0.8)
    
    # Add value labels
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2., val + 0.01,
                f'{val:.1f}%' if val < 1 else f'{val:.0f}%', 
                ha='center', va='bottom', fontsize=10)
    
    ax.set_ylabel('Absolute Agreement Rate')
    ax.set_title('Absolute Agreement: Set 1 vs Set 2', fontweight='bold')
    ax.set_ylim([0, 0.6])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.18, 'Exact match rates between LLM and human scores\\nSet 2 shows higher baseline agreement than Set 1',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 2: Spearman Correlation (Top Center)
    ax = axes[0, 1]
    spearman_values = [0.160, 0.185, 0.153, 0.211]
    p_values = ['p=0.000', 'p=0.051', 'p=0.000', 'p=0.029']
    
    bars = ax.bar(categories, spearman_values, color=colors, alpha=0.8)
    
    # Add value and p-value labels
    for i, (bar, val, p_val) in enumerate(zip(bars, spearman_values, p_values)):
        ax.text(bar.get_x() + bar.get_width()/2., val + 0.005,
                f'{val:.3f}\n({p_val})', ha='center', va='bottom', fontsize=9)
    
    ax.set_ylabel('Spearman ρ')
    ax.set_title('Spearman Correlation: Set 1 vs Set 2', fontweight='bold')
    ax.set_ylim([0, 0.25])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.18, 'Rank correlation between LLM and human ratings\\nMajority voting improves correlation in both sets',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 3: Within-One Agreement (Top Right)
    ax = axes[0, 2]
    within_one_values = [98.9, 98.2, 98.9, 100.0]
    
    bars = ax.bar(categories, within_one_values, color=colors, alpha=0.8)
    
    # Add value labels
    for bar, val in zip(bars, within_one_values):
        ax.text(bar.get_x() + bar.get_width()/2., val + 0.2,
                f'{val:.1f}%', ha='center', va='bottom', fontsize=10)
    
    ax.set_ylabel('Within-One Agreement')
    ax.set_title('Within-One Agreement: Set 1 vs Set 2', fontweight='bold')
    ax.set_ylim([98, 101])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.18, 'Percentage of LLM scores within ±1 of human scores\\nConsistently high across all conditions (>98%)',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # ========== ROW 2: Human Patterns and Summary ==========
    
    # Plot 4: Human Rater Voting Patterns (Bottom Left)
    ax = axes[1, 0]
    
    voting_types = ['Unanimous', 'Majority\nVoting Type', 'Tied']
    set1_percentages = [17.9, 79.5, 2.7]
    set2_percentages = [19.4, 74.1, 6.5]
    
    x = np.arange(len(voting_types))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, set1_percentages, width, label='Set 1', color='darkblue', alpha=0.8)
    bars2 = ax.bar(x + width/2, set2_percentages, width, label='Set 2', color='darkred', alpha=0.8)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height:.1f}%', ha='center', va='bottom', fontsize=9)
    
    ax.set_ylabel('Percentage')
    ax.set_title('Human Rater Voting Patterns', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(voting_types)
    ax.legend()
    ax.set_ylim([0, 90])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.18, 'Distribution of human rater agreement patterns\\nMost cases require majority voting to resolve disagreements',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 5: Dimension-wise Spearman Correlations (Bottom Center)
    ax = axes[1, 1]
    
    dimensions = ['Emotional\nReactions', 'Explorations', 'Interpretations', 'Empathy']
    set1_ind = [0.37, 0.42, 0.41, 0.40]
    set1_maj = [0.31, 0.21, 0.35, 0.57]
    set2_ind = [0.30, 0.37, 0.29, 0.39]
    set2_maj = [0.22, 0.22, 0.35, 0.57]
    
    x = np.arange(len(dimensions))
    width = 0.2
    
    ax.bar(x - 1.5*width, set1_ind, width, label='Set1 Ind', color='lightblue', alpha=0.8)
    ax.bar(x - 0.5*width, set1_maj, width, label='Set1 Maj', color='darkblue', alpha=0.8)
    ax.bar(x + 0.5*width, set2_ind, width, label='Set2 Ind', color='lightcoral', alpha=0.8)
    ax.bar(x + 1.5*width, set2_maj, width, label='Set2 Maj', color='darkred', alpha=0.8)
    
    ax.set_xlabel('Dimension')
    ax.set_ylabel('Spearman ρ')
    ax.set_title('Dimension-wise Spearman Correlations', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dimensions)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_ylim([0, 0.6])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.18, 'Correlation by empathy dimension and analysis method\\nEmpathy dimension shows highest correlation in both sets',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 6: Summary Table (Bottom Right)
    ax = axes[1, 2]
    ax.axis('tight')
    ax.axis('off')
    
    # Create summary table
    table_data = [
        ['Metric', 'Set 1', 'Set 2', 'Difference'],
        ['N Conversations', '28', '27', '-1'],
        ['', '', '', ''],
        ['Individual Analysis:', '', '', ''],
        ['Abs Agreement', '42.0%', '48.0%', '+6.0%'],
        ['Spearman ρ', '0.160', '0.153', '-0.007'],
        ['', '', '', ''],
        ['Majority Voting:', '', '', ''],
        ['Abs Agreement', '37.5%', '54.6%', '+17.1%'],
        ['Spearman ρ', '0.185', '0.211', '+0.026'],
        ['', '', '', ''],
        ['Impact of Majority:', '', '', ''],
        ['Δ Spearman (S1)', '+0.025', '', ''],
        ['Δ Spearman (S2)', '', '+0.058', '']
    ]
    
    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.2)
    
    # Style header and section headers
    for i in range(4):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Style section headers
    for row in [3, 7, 11]:
        table[(row, 0)].set_facecolor('#E6E6FA')
        table[(row, 0)].set_text_props(weight='bold')
    
    # Highlight improvements
    for row in [9, 12]:
        if row < len(table_data):
            table[(row, 3)].set_facecolor('#90EE90')
    
    ax.set_title('Summary Comparison', fontweight='bold', pad=20)
    
    # Add description
    ax.text(0.5, -0.12, 'Comprehensive numerical comparison between datasets\\nSet 2 shows larger improvements from majority voting',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Overall title and layout
    plt.suptitle('Set 1 vs Set 2: Impact of Majority Voting on LLM-Human Agreement\\nComparative Analysis Across Both Datasets', 
                fontsize=14, fontweight='bold', y=0.95)
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    
    return fig

def main():
    """Generate the annotated set comparison figure"""
    
    print("Creating annotated set comparison figure...")
    
    fig = create_annotated_set_comparison()
    
    output_file = 'annotated_set_comparison_analysis.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved annotated figure to: {output_file}")
    
    plt.show()

if __name__ == "__main__":
    main()