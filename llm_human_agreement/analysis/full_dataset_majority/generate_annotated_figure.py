#!/usr/bin/env python3
"""
Generate the annotated version of the complex majority voting analysis figure
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def create_annotated_majority_voting_figure():
    """Create the 9-panel figure with clear descriptions"""
    
    fig, axes = plt.subplots(3, 3, figsize=(18, 16))
    
    # ========== ROW 1: Main Agreement Metrics ==========
    
    # Plot 1: Agreement Rates (Top Left)
    ax = axes[0, 0]
    dimensions = ['Emotional\nReactions', 'Explorations', 'Interpretations', 'Empathy']
    absolute_agreement = [0.33, 0.64, 0.31, 0.56]
    within_one = [1.00, 0.96, 1.00, 1.00]
    
    x = np.arange(len(dimensions))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, absolute_agreement, width, label='Absolute (Majority)', 
                   color='steelblue', alpha=0.8)
    bars2 = ax.bar(x + width/2, within_one, width, label='Within ±1 (Majority)', 
                   color='lightcoral', alpha=0.8)
    
    # Add values
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                    f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Agreement Rate')
    ax.set_title('LLM-Human Agreement (After Majority Voting)', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dimensions)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1.1])
    
    # Add description
    ax.text(0.5, -0.20, 'Exact match (blue) and ±1 tolerance (red) rates\nafter resolving human disagreements via majority voting',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 2: Statistical Metrics (Top Center)
    ax = axes[0, 1]
    
    spearman = [0.25, 0.33, 0.38, 0.45]
    pearson = [0.29, 0.38, 0.41, 0.47]
    kappa = [0.05, 0.11, -0.00, 0.28]
    
    x = np.arange(len(dimensions))
    width = 0.25
    
    ax.bar(x - width, spearman, width, label='Spearman ρ', color='darkgreen')
    ax.bar(x, pearson, width, label='Pearson r', color='darkblue')
    ax.bar(x + width, kappa, width, label="Cohen's κ", color='purple')
    
    # Add values
    for i, (s, p, k) in enumerate(zip(spearman, pearson, kappa)):
        ax.text(i - width, s + 0.01, f'{s:.2f}', ha='center', va='bottom', fontsize=8)
        ax.text(i, p + 0.01, f'{p:.2f}', ha='center', va='bottom', fontsize=8)
        ax.text(i + width, k + 0.01, f'{k:.2f}', ha='center', va='bottom', fontsize=8)
    
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Correlation/Agreement Coefficient')
    ax.set_title('Statistical Agreement Metrics', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dimensions)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([-0.1, 0.6])
    
    # Add description
    ax.text(0.5, -0.20, 'Three statistical measures: Spearman/Pearson correlations\nand Cohen\'s κ for classification agreement',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 3: Human Inter-rater Agreement (Top Right)
    ax = axes[0, 2]
    
    human_agreement = [73.09, 75.27, 71.64, 74.91]
    
    bars = ax.bar(dimensions, human_agreement, color='teal', alpha=0.8)
    
    for bar, val in zip(bars, human_agreement):
        ax.text(bar.get_x() + bar.get_width()/2., val + 1,
                f'{val:.1f}%', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Average Human Agreement Rate')
    ax.set_title('Human Inter-rater Agreement\n(Before Majority Voting)', fontweight='bold')
    ax.set_ylim([0, 100])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.20, 'Human evaluators agreed ~73-75% of the time,\nshowing need for majority voting to resolve disagreements',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # ========== ROW 2: Confusion Matrices ==========
    
    # Create confusion matrices for first 3 dimensions
    confusion_data = [
        ([[1, 3, 0], [6, 15, 11], [0, 14, 3]], 'Emotional Reactions', 0.048),
        ([[2, 2, 0], [2, 13, 2], [0, 1, 11]], 'Explorations', 0.113),
        ([[0, 2, 0], [0, 18, 2], [0, 10, 30]], 'Interpretations', -0.002)
    ]
    
    for idx, (matrix_data, dim_name, kappa_val) in enumerate(confusion_data):
        ax = axes[1, idx]
        
        matrix = np.array(matrix_data)
        matrix_norm = matrix / matrix.sum() * 100  # Convert to percentages
        
        im = ax.imshow(matrix_norm, cmap='YlOrRd', vmin=0, vmax=50)
        
        # Add text
        for i in range(3):
            for j in range(3):
                text = ax.text(j, i, f'{matrix[i,j]}\n({matrix_norm[i,j]:.0f}%)',
                             ha="center", va="center", color="black", fontsize=9)
        
        ax.set_xticks([0, 1, 2])
        ax.set_yticks([0, 1, 2])
        ax.set_xlabel('LLM Score')
        ax.set_ylabel('Human Score (Majority)')
        ax.set_title(f'{dim_name}\n(κ={kappa_val:.3f})', fontweight='bold')
        
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        
        # Add description
        ax.text(0.5, -0.25, 'Score distribution: darker = more frequent\nDiagonal = perfect LLM-human agreement',
               transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # ========== ROW 3: Overall Comparisons ==========
    
    # Plot 7: Before/After Comparison (Bottom Left)
    ax = axes[2, 0]
    
    metrics = ['Absolute\nAgreement', 'Spearman ρ', 'Within ±1']
    individual = [0.424, 0.174, 0.987]
    majority = [0.459, 0.351, 0.991]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, individual, width, label='Individual Ratings', 
                   color='lightgray', alpha=0.8)
    bars2 = ax.bar(x + width/2, majority, width, label='Majority Voting', 
                   color='darkblue', alpha=0.8)
    
    # Add value labels and improvement percentages
    for i, (ind, maj) in enumerate(zip(individual, majority)):
        ax.text(i - width/2, ind + 0.01, f'{ind:.3f}', ha='center', va='bottom', fontsize=9)
        ax.text(i + width/2, maj + 0.01, f'{maj:.3f}', ha='center', va='bottom', fontsize=9)
        
        improvement = ((maj - ind) / ind) * 100
        ax.text(i, max(ind, maj) + 0.05, f'+{improvement:.0f}%', 
                ha='center', va='bottom', fontsize=9, color='green', fontweight='bold')
    
    ax.set_ylabel('Score')
    ax.set_title('Impact of Majority Voting on Agreement Metrics', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1.2])
    
    # Add description
    ax.text(0.5, -0.20, 'Before vs after majority voting\nGreen % = improvement achieved',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 8: Summary Table (Bottom Center)
    ax = axes[2, 1]
    ax.axis('tight')
    ax.axis('off')
    
    table_data = [
        ['Metric', 'Individual', 'Majority', 'Change'],
        ['Abs. Agreement', '0.424', '0.459', '+0.035'],
        ['Spearman ρ', '0.174', '0.351', '+0.177'],
        ['Within ±1', '0.987', '0.991', '+0.004']
    ]
    
    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    
    # Style header
    for i in range(4):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Highlight improvements (green for positive changes)
    for i in range(1, 4):
        table[(i, 3)].set_facecolor('#90EE90')
    
    ax.set_title('Overall Comparison', fontweight='bold', pad=20)
    
    # Add description
    ax.text(0.5, -0.15, 'Numerical summary of all improvements\nGreen = positive changes from majority voting',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 9: Human Agreement by Dimension (Bottom Right)
    ax = axes[2, 2]
    
    human_dim_agreement = [73.09, 75.27, 71.64, 74.91]
    
    bars = ax.bar(dimensions, human_dim_agreement, color='coral', alpha=0.8)
    
    for bar, val in zip(bars, human_dim_agreement):
        ax.text(bar.get_x() + bar.get_width()/2., val + 1,
                f'{val:.0f}%', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Dimension')
    ax.set_ylabel('Avg Human Agreement')
    ax.set_title('Human Agreement by Dimension', fontweight='bold')
    ax.set_ylim([0, 100])
    ax.grid(True, alpha=0.3)
    
    # Add description
    ax.text(0.5, -0.20, 'Human evaluator consistency by dimension\n~25% disagreement requires majority resolution',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Overall title and layout
    plt.suptitle('LLM-Human Agreement Analysis with Majority Voting\nComprehensive Results for 55 Conversations', 
                fontsize=14, fontweight='bold', y=0.97)
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for title and descriptions
    
    return fig

def main():
    """Generate the annotated figure"""
    
    print("Creating annotated majority voting analysis figure...")
    
    fig = create_annotated_majority_voting_figure()
    
    output_file = 'annotated_majority_voting_analysis.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved annotated figure to: {output_file}")
    
    plt.show()

if __name__ == "__main__":
    main()