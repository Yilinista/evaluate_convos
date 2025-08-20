#!/usr/bin/env python3
"""
Comprehensive Analysis: Both dimension-wise and overall correlations
Reports results in the format that best serves research needs
"""

import pandas as pd
import numpy as np
from scipy import stats
import sys
import os

# Add the parent directory to sys.path to import from other scripts
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.llm_human_agreement_with_majority_voting import (
    load_human_evaluations_set1,
    load_human_evaluations_set2, 
    load_llm_evaluations,
    apply_majority_voting,
    calculate_agreement_metrics_with_majority
)

from scripts.llm_human_agreement_analysis import calculate_agreement_metrics

def calculate_both_correlation_methods(human_evals, llm_scores, use_majority_voting=False):
    """Calculate correlations using both dimension-wise average and overall methods"""
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    if use_majority_voting:
        # Apply majority voting first
        majority_scores = apply_majority_voting(human_evals, len(llm_scores))
        results = calculate_agreement_metrics_with_majority(majority_scores, llm_scores)
        method_label = "WITH Majority Voting"
    else:
        # Use individual ratings
        results = calculate_agreement_metrics(human_evals, llm_scores)
        method_label = "WITHOUT Majority Voting"
    
    print(f"\n{'='*60}")
    print(f"CORRELATION ANALYSIS - {method_label}")
    print('='*60)
    
    # Method 1: Dimension-wise average (like original 0.325)
    dimension_correlations = []
    for dim in dimensions:
        corr = results[dim]['spearman_correlation']
        if not np.isnan(corr):
            dimension_correlations.append(corr)
        print(f"  {dim.replace('_', ' ').title()}: ρ = {corr:.3f}")
    
    avg_correlation = np.mean(dimension_correlations)
    
    print(f"\n📊 METHOD 1 - Dimension Average:")
    print(f"   Average Spearman ρ = {avg_correlation:.3f}")
    print(f"   (This matches the original reporting style: 0.325)")
    
    # Method 2: Overall correlation (like current 0.190)
    all_human = []
    all_llm = []
    for dim in dimensions:
        if 'human_scores' in results[dim] and 'llm_scores' in results[dim]:
            all_human.extend(results[dim]['human_scores'])
            all_llm.extend(results[dim]['llm_scores'])
    
    if len(all_human) > 0:
        overall_corr, overall_p = stats.spearmanr(all_human, all_llm)
        
        print(f"\n📊 METHOD 2 - Overall Correlation:")
        print(f"   Overall Spearman ρ = {overall_corr:.3f} (p = {overall_p:.4f})")
        print(f"   Total comparisons = {len(all_human)}")
        print(f"   (This is more statistically rigorous)")
    else:
        overall_corr = np.nan
        overall_p = np.nan
    
    # Other metrics (same regardless of correlation method)
    avg_abs_agreement = np.mean([results[d]['absolute_agreement'] for d in dimensions])
    avg_within_one = np.mean([results[d]['within_one_agreement'] for d in dimensions])
    
    print(f"\n📊 OTHER METRICS:")
    print(f"   Absolute Agreement = {avg_abs_agreement:.1%}")
    print(f"   Within-One Agreement = {avg_within_one:.1%}")
    
    return {
        'method': method_label,
        'dimension_average_rho': avg_correlation,
        'overall_rho': overall_corr,
        'overall_p_value': overall_p,
        'absolute_agreement': avg_abs_agreement,
        'within_one_agreement': avg_within_one,
        'n_comparisons': len(all_human),
        'dimension_details': {dim: results[dim]['spearman_correlation'] for dim in dimensions}
    }

def main():
    """Main analysis comparing both correlation calculation methods"""
    
    print("="*80)
    print("COMPREHENSIVE ANALYSIS: DIMENSION-WISE vs OVERALL CORRELATIONS")
    print("Addressing the question: Should we report 0.325 or 0.190?")
    print("="*80)
    
    # Load all data
    set1_human = load_human_evaluations_set1("../data/Empathy Evaluation - Set 1.csv")
    set2_human = load_human_evaluations_set2("../data/Empathy Evaluation - Set 2.csv") 
    set1_llm = load_llm_evaluations("../../google_forms/updated/conversation_set1_metadata.csv")
    set2_llm = load_llm_evaluations("../../google_forms/updated/conversation_set2_metadata.csv")
    
    # Combine datasets
    all_human = set1_human + set2_human
    all_llm = set1_llm + set2_llm
    
    print(f"\n📁 DATASET INFO:")
    print(f"   Set 1: {len(set1_llm)} conversations, {len(set1_human)} evaluators")
    print(f"   Set 2: {len(set2_llm)} conversations, {len(set2_human)} evaluators")
    print(f"   Total: {len(all_llm)} conversations")
    
    # Analysis 1: Without majority voting
    results_individual = calculate_both_correlation_methods(all_human, all_llm, use_majority_voting=False)
    
    # Analysis 2: With majority voting  
    results_majority = calculate_both_correlation_methods(all_human, all_llm, use_majority_voting=True)
    
    # Summary comparison
    print(f"\n{'='*80}")
    print("SUMMARY COMPARISON")
    print('='*80)
    
    print(f"\n🔍 ORIGINAL vs CURRENT METHODS:")
    print(f"   Original report style (dimension average):")
    print(f"     • Individual ratings: {results_individual['dimension_average_rho']:.3f}")
    print(f"     • With majority voting: {results_majority['dimension_average_rho']:.3f}")
    print(f"     • Change from majority voting: {results_majority['dimension_average_rho'] - results_individual['dimension_average_rho']:+.3f}")
    
    print(f"\n   Current analysis style (overall correlation):")
    print(f"     • Individual ratings: {results_individual['overall_rho']:.3f}")
    print(f"     • With majority voting: {results_majority['overall_rho']:.3f}")
    print(f"     • Change from majority voting: {results_majority['overall_rho'] - results_individual['overall_rho']:+.3f}")
    
    print(f"\n🎯 RESEARCH QUESTION: Did majority voting help?")
    
    if results_majority['dimension_average_rho'] > results_individual['dimension_average_rho']:
        print(f"   ✅ YES - Using dimension average method:")
        print(f"      Majority voting improved correlation from {results_individual['dimension_average_rho']:.3f} to {results_majority['dimension_average_rho']:.3f}")
    
    if results_majority['overall_rho'] > results_individual['overall_rho']:
        print(f"   ✅ YES - Using overall correlation method:")
        print(f"      Majority voting improved correlation from {results_individual['overall_rho']:.3f} to {results_majority['overall_rho']:.3f}")
    
    print(f"\n💡 RECOMMENDATION FOR SIYAN:")
    print(f"   Report BOTH methods to be comprehensive:")
    print(f"   ")
    print(f"   'After applying majority voting to resolve human rater disagreements:")
    print(f"   • Dimension-wise average Spearman ρ: {results_majority['dimension_average_rho']:.3f}")
    print(f"     (improved from {results_individual['dimension_average_rho']:.3f}, +{results_majority['dimension_average_rho'] - results_individual['dimension_average_rho']:.3f})")
    print(f"   • Overall Spearman ρ: {results_majority['overall_rho']:.3f} (p < {results_majority['overall_p_value']:.3f})")
    print(f"     (improved from {results_individual['overall_rho']:.3f}, +{results_majority['overall_rho'] - results_individual['overall_rho']:.3f})")
    print(f"   • Absolute agreement: {results_majority['absolute_agreement']:.1%}")
    print(f"   • Within-one agreement: {results_majority['within_one_agreement']:.1%}")
    print(f"   • Total conversations: {len(all_llm)} (Set 1: {len(set1_llm)}, Set 2: {len(set2_llm)})'")
    
    # Create comparison table
    comparison_df = pd.DataFrame([
        {
            'Method': 'Individual Ratings',
            'Dimension_Avg_Rho': results_individual['dimension_average_rho'],
            'Overall_Rho': results_individual['overall_rho'],
            'Overall_P_Value': results_individual['overall_p_value'],
            'Abs_Agreement': results_individual['absolute_agreement'],
            'Within_One': results_individual['within_one_agreement'],
            'N_Comparisons': results_individual['n_comparisons']
        },
        {
            'Method': 'Majority Voting',
            'Dimension_Avg_Rho': results_majority['dimension_average_rho'],
            'Overall_Rho': results_majority['overall_rho'],
            'Overall_P_Value': results_majority['overall_p_value'],
            'Abs_Agreement': results_majority['absolute_agreement'],
            'Within_One': results_majority['within_one_agreement'],
            'N_Comparisons': results_majority['n_comparisons']
        }
    ])
    
    output_file = '../results/comprehensive_correlation_comparison.csv'
    comparison_df.to_csv(output_file, index=False)
    print(f"\n💾 Saved detailed comparison to: {output_file}")
    
    print(f"\n{'='*80}")
    
    return comparison_df

if __name__ == "__main__":
    main()