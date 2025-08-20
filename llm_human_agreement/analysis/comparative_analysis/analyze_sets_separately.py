#!/usr/bin/env python3
"""
Separate analysis of Set 1 and Set 2 to identify source of metric changes
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Import functions from existing scripts
from llm_human_agreement_analysis import (
    load_human_evaluations, 
    load_llm_evaluations,
    calculate_agreement_metrics,
    convert_rating
)

from llm_human_agreement_with_majority_voting import (
    apply_majority_voting,
    calculate_agreement_metrics_with_majority
)

def analyze_single_set(set_name, human_eval_path, llm_metadata_path):
    """Analyze a single set with and without majority voting"""
    
    print(f"\n{'='*60}")
    print(f"ANALYZING {set_name}")
    print('='*60)
    
    # Load data
    human_evals = load_human_evaluations(human_eval_path)
    llm_scores = load_llm_evaluations(llm_metadata_path)
    
    print(f"Loaded {len(human_evals)} human evaluators")
    print(f"Loaded {len(llm_scores)} conversations")
    
    # Calculate WITHOUT majority voting
    print(f"\n{set_name} - WITHOUT Majority Voting:")
    print("-"*40)
    results_individual = calculate_agreement_metrics(human_evals, llm_scores)
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    # Calculate overall metrics for individual
    individual_abs_agreement = np.mean([results_individual[d]['absolute_agreement'] for d in dimensions])
    individual_spearman = np.mean([results_individual[d]['spearman_correlation'] for d in dimensions])
    individual_within_one = np.mean([results_individual[d]['within_one_agreement'] for d in dimensions])
    
    # Calculate overall Spearman directly
    all_human_ind = []
    all_llm_ind = []
    for d in dimensions:
        all_human_ind.extend(results_individual[d]['human_scores'])
        all_llm_ind.extend(results_individual[d]['llm_scores'])
    overall_spearman_ind, p_val_ind = stats.spearmanr(all_human_ind, all_llm_ind)
    
    print(f"  Absolute Agreement: {individual_abs_agreement:.1%}")
    print(f"  Spearman ρ (avg): {individual_spearman:.3f}")
    print(f"  Spearman ρ (overall): {overall_spearman_ind:.3f} (p={p_val_ind:.4f})")
    print(f"  Within-one Agreement: {individual_within_one:.1%}")
    
    # Dimension-wise details
    print("\n  By Dimension:")
    for dim in dimensions:
        print(f"    {dim.replace('_', ' ').title()}:")
        print(f"      Abs Agreement: {results_individual[dim]['absolute_agreement']:.1%}")
        print(f"      Spearman ρ: {results_individual[dim]['spearman_correlation']:.3f}")
        print(f"      N comparisons: {results_individual[dim]['n_comparisons']}")
    
    # Calculate WITH majority voting
    print(f"\n{set_name} - WITH Majority Voting:")
    print("-"*40)
    
    majority_scores = apply_majority_voting(human_evals, len(llm_scores))
    results_majority = calculate_agreement_metrics_with_majority(majority_scores, llm_scores)
    
    # Calculate overall metrics for majority
    majority_abs_agreement = np.mean([results_majority[d]['absolute_agreement'] for d in dimensions])
    majority_spearman = np.mean([results_majority[d]['spearman_correlation'] for d in dimensions])
    majority_within_one = np.mean([results_majority[d]['within_one_agreement'] for d in dimensions])
    
    # Calculate overall Spearman directly
    all_human_maj = []
    all_llm_maj = []
    for d in dimensions:
        all_human_maj.extend(results_majority[d]['human_scores'])
        all_llm_maj.extend(results_majority[d]['llm_scores'])
    overall_spearman_maj, p_val_maj = stats.spearmanr(all_human_maj, all_llm_maj)
    
    print(f"  Absolute Agreement: {majority_abs_agreement:.1%}")
    print(f"  Spearman ρ (avg): {majority_spearman:.3f}")
    print(f"  Spearman ρ (overall): {overall_spearman_maj:.3f} (p={p_val_maj:.4f})")
    print(f"  Within-one Agreement: {majority_within_one:.1%}")
    
    # Dimension-wise details
    print("\n  By Dimension:")
    for dim in dimensions:
        print(f"    {dim.replace('_', ' ').title()}:")
        print(f"      Abs Agreement: {results_majority[dim]['absolute_agreement']:.1%}")
        print(f"      Spearman ρ: {results_majority[dim]['spearman_correlation']:.3f}")
        print(f"      Human Agreement: {results_majority[dim]['avg_human_agreement']:.1%}")
    
    # Calculate voting statistics
    voting_stats = {dim: {'unanimous': 0, 'majority': 0, 'tied': 0, 'total': 0} 
                   for dim in dimensions}
    
    for conv in majority_scores:
        for dim in dimensions:
            if conv[dim] is not None:
                votes_key = f'{dim}_votes'
                if votes_key in conv:
                    vote_counts = list(conv[votes_key].values())
                    total_votes = sum(vote_counts)
                    max_votes = max(vote_counts)
                    
                    voting_stats[dim]['total'] += 1
                    
                    if len(vote_counts) == 1 or max_votes == total_votes:
                        voting_stats[dim]['unanimous'] += 1
                    elif vote_counts.count(max_votes) > 1:
                        voting_stats[dim]['tied'] += 1
                    else:
                        voting_stats[dim]['majority'] += 1
    
    print(f"\n{set_name} - Voting Statistics:")
    print("-"*40)
    avg_unanimous = np.mean([voting_stats[d]['unanimous']/voting_stats[d]['total']*100 
                             for d in dimensions if voting_stats[d]['total'] > 0])
    avg_majority = np.mean([voting_stats[d]['majority']/voting_stats[d]['total']*100 
                           for d in dimensions if voting_stats[d]['total'] > 0])
    avg_tied = np.mean([voting_stats[d]['tied']/voting_stats[d]['total']*100 
                       for d in dimensions if voting_stats[d]['total'] > 0])
    
    print(f"  Average Unanimous: {avg_unanimous:.1f}%")
    print(f"  Average Majority: {avg_majority:.1f}%")
    print(f"  Average Tied: {avg_tied:.1f}%")
    
    # Impact of majority voting
    print(f"\n{set_name} - Impact of Majority Voting:")
    print("-"*40)
    print(f"  Absolute Agreement: {individual_abs_agreement:.1%} → {majority_abs_agreement:.1%} ({majority_abs_agreement - individual_abs_agreement:+.1%})")
    print(f"  Spearman ρ (overall): {overall_spearman_ind:.3f} → {overall_spearman_maj:.3f} ({overall_spearman_maj - overall_spearman_ind:+.3f})")
    print(f"  Within-one: {individual_within_one:.1%} → {majority_within_one:.1%} ({majority_within_one - individual_within_one:+.1%})")
    
    return {
        'set_name': set_name,
        'n_conversations': len(llm_scores),
        'n_evaluators': len(human_evals),
        'individual': {
            'abs_agreement': individual_abs_agreement,
            'spearman_avg': individual_spearman,
            'spearman_overall': overall_spearman_ind,
            'p_value': p_val_ind,
            'within_one': individual_within_one,
            'by_dimension': results_individual
        },
        'majority': {
            'abs_agreement': majority_abs_agreement,
            'spearman_avg': majority_spearman,
            'spearman_overall': overall_spearman_maj,
            'p_value': p_val_maj,
            'within_one': majority_within_one,
            'by_dimension': results_majority
        },
        'voting_stats': {
            'unanimous_pct': avg_unanimous,
            'majority_pct': avg_majority,
            'tied_pct': avg_tied
        }
    }

def create_comparison_visualization(set1_results, set2_results):
    """Create visualization comparing Set 1 and Set 2"""
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    
    # Plot 1: Absolute Agreement Comparison
    ax = axes[0, 0]
    
    categories = ['Set 1\nIndividual', 'Set 1\nMajority', 'Set 2\nIndividual', 'Set 2\nMajority']
    abs_agreements = [
        set1_results['individual']['abs_agreement'],
        set1_results['majority']['abs_agreement'],
        set2_results['individual']['abs_agreement'],
        set2_results['majority']['abs_agreement']
    ]
    
    colors = ['lightblue', 'darkblue', 'lightcoral', 'darkred']
    bars = ax.bar(categories, abs_agreements, color=colors)
    
    # Add value labels
    for bar, val in zip(bars, abs_agreements):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
               f'{val:.1%}', ha='center', va='bottom')
    
    ax.set_ylabel('Absolute Agreement')
    ax.set_title('Absolute Agreement: Set 1 vs Set 2')
    ax.set_ylim([0, 1])
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Spearman Correlation Comparison
    ax = axes[0, 1]
    
    spearman_values = [
        set1_results['individual']['spearman_overall'],
        set1_results['majority']['spearman_overall'],
        set2_results['individual']['spearman_overall'],
        set2_results['majority']['spearman_overall']
    ]
    
    bars = ax.bar(categories, spearman_values, color=colors)
    
    # Add value labels with p-values
    p_values = [
        set1_results['individual']['p_value'],
        set1_results['majority']['p_value'],
        set2_results['individual']['p_value'],
        set2_results['majority']['p_value']
    ]
    
    for bar, val, p in zip(bars, spearman_values, p_values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
               f'{val:.3f}\n(p={p:.3f})', ha='center', va='bottom')
    
    ax.set_ylabel('Spearman ρ')
    ax.set_title('Spearman Correlation: Set 1 vs Set 2')
    ax.set_ylim([0, max(spearman_values) * 1.2])
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Within-One Agreement
    ax = axes[0, 2]
    
    within_one_values = [
        set1_results['individual']['within_one'],
        set1_results['majority']['within_one'],
        set2_results['individual']['within_one'],
        set2_results['majority']['within_one']
    ]
    
    bars = ax.bar(categories, within_one_values, color=colors)
    
    for bar, val in zip(bars, within_one_values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
               f'{val:.1%}', ha='center', va='bottom')
    
    ax.set_ylabel('Within-One Agreement')
    ax.set_title('Within-One Agreement: Set 1 vs Set 2')
    ax.set_ylim([0.9, 1.01])
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Voting Statistics
    ax = axes[1, 0]
    
    voting_categories = ['Unanimous', 'Majority', 'Tied']
    x = np.arange(len(voting_categories))
    width = 0.35
    
    set1_voting = [
        set1_results['voting_stats']['unanimous_pct'],
        set1_results['voting_stats']['majority_pct'],
        set1_results['voting_stats']['tied_pct']
    ]
    
    set2_voting = [
        set2_results['voting_stats']['unanimous_pct'],
        set2_results['voting_stats']['majority_pct'],
        set2_results['voting_stats']['tied_pct']
    ]
    
    bars1 = ax.bar(x - width/2, set1_voting, width, label='Set 1', color='darkblue')
    bars2 = ax.bar(x + width/2, set2_voting, width, label='Set 2', color='darkred')
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=9)
    
    ax.set_ylabel('Percentage')
    ax.set_xlabel('Voting Type')
    ax.set_title('Human Rater Voting Patterns')
    ax.set_xticks(x)
    ax.set_xticklabels(voting_categories)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 5: Dimension-wise Spearman Comparison
    ax = axes[1, 1]
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    dim_labels = [d.replace('_', '\n').title() for d in dimensions]
    
    x = np.arange(len(dimensions))
    width = 0.2
    
    # Get dimension-wise Spearman correlations
    set1_ind = [set1_results['individual']['by_dimension'][d]['spearman_correlation'] for d in dimensions]
    set1_maj = [set1_results['majority']['by_dimension'][d]['spearman_correlation'] for d in dimensions]
    set2_ind = [set2_results['individual']['by_dimension'][d]['spearman_correlation'] for d in dimensions]
    set2_maj = [set2_results['majority']['by_dimension'][d]['spearman_correlation'] for d in dimensions]
    
    ax.bar(x - 1.5*width, set1_ind, width, label='Set1 Ind', color='lightblue')
    ax.bar(x - 0.5*width, set1_maj, width, label='Set1 Maj', color='darkblue')
    ax.bar(x + 0.5*width, set2_ind, width, label='Set2 Ind', color='lightcoral')
    ax.bar(x + 1.5*width, set2_maj, width, label='Set2 Maj', color='darkred')
    
    ax.set_ylabel('Spearman ρ')
    ax.set_xlabel('Dimension')
    ax.set_title('Dimension-wise Spearman Correlations')
    ax.set_xticks(x)
    ax.set_xticklabels(dim_labels)
    ax.legend(ncol=2, fontsize=9)
    ax.grid(True, alpha=0.3)
    
    # Plot 6: Summary Table
    ax = axes[1, 2]
    ax.axis('tight')
    ax.axis('off')
    
    table_data = [
        ['Metric', 'Set 1', 'Set 2', 'Difference'],
        ['N Conversations', str(set1_results['n_conversations']), 
         str(set2_results['n_conversations']), 
         str(set2_results['n_conversations'] - set1_results['n_conversations'])],
        ['', '', '', ''],
        ['Individual Analysis:', '', '', ''],
        ['  Abs Agreement', f"{set1_results['individual']['abs_agreement']:.1%}",
         f"{set2_results['individual']['abs_agreement']:.1%}",
         f"{(set2_results['individual']['abs_agreement'] - set1_results['individual']['abs_agreement']):.1%}"],
        ['  Spearman ρ', f"{set1_results['individual']['spearman_overall']:.3f}",
         f"{set2_results['individual']['spearman_overall']:.3f}",
         f"{(set2_results['individual']['spearman_overall'] - set1_results['individual']['spearman_overall']):+.3f}"],
        ['', '', '', ''],
        ['Majority Voting:', '', '', ''],
        ['  Abs Agreement', f"{set1_results['majority']['abs_agreement']:.1%}",
         f"{set2_results['majority']['abs_agreement']:.1%}",
         f"{(set2_results['majority']['abs_agreement'] - set1_results['majority']['abs_agreement']):.1%}"],
        ['  Spearman ρ', f"{set1_results['majority']['spearman_overall']:.3f}",
         f"{set2_results['majority']['spearman_overall']:.3f}",
         f"{(set2_results['majority']['spearman_overall'] - set1_results['majority']['spearman_overall']):+.3f}"],
        ['', '', '', ''],
        ['Impact of Majority:', '', '', ''],
        ['  Δ Spearman (S1)', 
         f"{(set1_results['majority']['spearman_overall'] - set1_results['individual']['spearman_overall']):+.3f}",
         '', ''],
        ['  Δ Spearman (S2)', '',
         f"{(set2_results['majority']['spearman_overall'] - set2_results['individual']['spearman_overall']):+.3f}",
         '']
    ]
    
    table = ax.table(cellText=table_data, loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.5)
    
    # Header styling
    for i in range(len(table_data[0])):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Section headers
    for row_idx in [3, 7, 11]:
        for col_idx in range(4):
            table[(row_idx, col_idx)].set_facecolor('#e0e0e0')
            table[(row_idx, col_idx)].set_text_props(weight='bold')
    
    ax.set_title('Summary Comparison', fontweight='bold', pad=20)
    
    plt.suptitle('Set 1 vs Set 2: Impact of Majority Voting on LLM-Human Agreement', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    return fig

def main():
    """Main analysis function"""
    
    print("="*80)
    print("SEPARATE ANALYSIS: SET 1 vs SET 2")
    print("Comparing Individual Ratings vs Majority Voting Impact")
    print("="*80)
    
    # Paths
    set1_human_path = "data/Empathy Evaluation - Set 1.csv"
    set2_human_path = "data/Empathy Evaluation - Set 2.csv"
    set1_llm_path = "../google_forms/updated/conversation_set1_metadata.csv"
    set2_llm_path = "../google_forms/updated/conversation_set2_metadata.csv"
    
    # Check files exist
    from pathlib import Path
    if not Path(set1_human_path).exists():
        print(f"ERROR: {set1_human_path} not found!")
        return
    if not Path(set2_human_path).exists():
        print(f"ERROR: {set2_human_path} not found!")
        return
    
    # Analyze each set
    set1_results = analyze_single_set("SET 1", set1_human_path, set1_llm_path)
    set2_results = analyze_single_set("SET 2", set2_human_path, set2_llm_path)
    
    # Create comparison visualization
    print("\n" + "="*80)
    print("CREATING COMPARISON VISUALIZATION")
    print("="*80)
    
    fig = create_comparison_visualization(set1_results, set2_results)
    output_file = 'set_comparison_analysis.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved visualization to {output_file}")
    
    # Final comparison summary
    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80)
    
    print("\n1. DATASET DIFFERENCES (Without Majority Voting):")
    print("-"*50)
    spear_diff_ind = set2_results['individual']['spearman_overall'] - set1_results['individual']['spearman_overall']
    abs_diff_ind = set2_results['individual']['abs_agreement'] - set1_results['individual']['abs_agreement']
    
    print(f"   Set 1 Spearman ρ: {set1_results['individual']['spearman_overall']:.3f}")
    print(f"   Set 2 Spearman ρ: {set2_results['individual']['spearman_overall']:.3f}")
    print(f"   Difference: {spear_diff_ind:+.3f}")
    
    if abs(spear_diff_ind) > 0.1:
        print(f"   ⚠ Significant difference between datasets!")
    else:
        print(f"   ✓ Datasets are relatively similar")
    
    print("\n2. IMPACT OF MAJORITY VOTING:")
    print("-"*50)
    set1_impact = set1_results['majority']['spearman_overall'] - set1_results['individual']['spearman_overall']
    set2_impact = set2_results['majority']['spearman_overall'] - set2_results['individual']['spearman_overall']
    
    print(f"   Set 1: {set1_results['individual']['spearman_overall']:.3f} → {set1_results['majority']['spearman_overall']:.3f} ({set1_impact:+.3f})")
    print(f"   Set 2: {set2_results['individual']['spearman_overall']:.3f} → {set2_results['majority']['spearman_overall']:.3f} ({set2_impact:+.3f})")
    
    print("\n3. ROOT CAUSE ANALYSIS:")
    print("-"*50)
    
    # Calculate combined results for comparison with original
    combined_n = set1_results['n_conversations'] + set2_results['n_conversations']
    combined_spearman_ind = (set1_results['individual']['spearman_overall'] * set1_results['n_conversations'] + 
                             set2_results['individual']['spearman_overall'] * set2_results['n_conversations']) / combined_n
    combined_spearman_maj = (set1_results['majority']['spearman_overall'] * set1_results['n_conversations'] + 
                             set2_results['majority']['spearman_overall'] * set2_results['n_conversations']) / combined_n
    
    print(f"   Original reported (Set 1 subset): 0.325")
    print(f"   Set 1 only (28 convos): {set1_results['individual']['spearman_overall']:.3f}")
    print(f"   Set 2 only (27 convos): {set2_results['individual']['spearman_overall']:.3f}")
    print(f"   Combined (55 convos, individual): ~{combined_spearman_ind:.3f}")
    print(f"   Combined (55 convos, majority): ~{combined_spearman_maj:.3f}")
    
    # Determine primary cause
    print("\n   CONCLUSION:")
    if abs(spear_diff_ind) > abs(set1_impact) and abs(spear_diff_ind) > abs(set2_impact):
        print("   → Primary cause: DATASET DIFFERENCES")
        print(f"     Set 2 has inherently lower agreement ({spear_diff_ind:+.3f})")
    elif abs(set1_impact) > 0.05 or abs(set2_impact) > 0.05:
        print("   → Primary cause: MAJORITY VOTING IMPACT")
        print(f"     Majority voting changed correlations significantly")
    else:
        print("   → Mixed causes: Both dataset differences and majority voting contribute")
    
    # Save detailed results to CSV
    results_df = pd.DataFrame([
        {
            'Set': 'Set 1',
            'N_Conversations': set1_results['n_conversations'],
            'Abs_Agreement_Individual': set1_results['individual']['abs_agreement'],
            'Abs_Agreement_Majority': set1_results['majority']['abs_agreement'],
            'Spearman_Individual': set1_results['individual']['spearman_overall'],
            'Spearman_Majority': set1_results['majority']['spearman_overall'],
            'P_Value_Individual': set1_results['individual']['p_value'],
            'P_Value_Majority': set1_results['majority']['p_value'],
            'Unanimous_Pct': set1_results['voting_stats']['unanimous_pct'],
            'Majority_Vote_Pct': set1_results['voting_stats']['majority_pct']
        },
        {
            'Set': 'Set 2',
            'N_Conversations': set2_results['n_conversations'],
            'Abs_Agreement_Individual': set2_results['individual']['abs_agreement'],
            'Abs_Agreement_Majority': set2_results['majority']['abs_agreement'],
            'Spearman_Individual': set2_results['individual']['spearman_overall'],
            'Spearman_Majority': set2_results['majority']['spearman_overall'],
            'P_Value_Individual': set2_results['individual']['p_value'],
            'P_Value_Majority': set2_results['majority']['p_value'],
            'Unanimous_Pct': set2_results['voting_stats']['unanimous_pct'],
            'Majority_Vote_Pct': set2_results['voting_stats']['majority_pct']
        }
    ])
    
    output_csv = 'set_comparison_summary.csv'
    results_df.to_csv(output_csv, index=False)
    print(f"\n✓ Saved detailed results to {output_csv}")
    
    print("\n" + "="*80)
    
    plt.show()

if __name__ == "__main__":
    main()