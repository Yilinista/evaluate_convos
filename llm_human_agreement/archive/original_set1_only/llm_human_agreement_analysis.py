#!/usr/bin/env python3
"""
LLM-Human Agreement Analysis for Empathy Evaluation
Measures absolute agreement rates and Spearman correlations between LLM and human judgments
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
from collections import defaultdict
import krippendorff

def load_human_evaluations(csv_path):
    """Load and parse human evaluation data from Google Forms CSV"""
    df = pd.read_csv(csv_path)
    
    # The CSV has multiple columns for each conversation
    # Column pattern: "Emotional Reactions", "Explorations", "Interpretations", "Overall Empathy" repeated
    
    # Get all evaluators (rows)
    evaluators = []
    
    for idx, row in df.iterrows():
        evaluator_data = {
            'evaluator_id': row['What is your Prolific ID?'],
            'timestamp': row['Timestamp'],
            'conversations': []
        }
        
        # Parse each conversation's ratings
        # Columns start from index 2 (after timestamp and ID)
        cols = df.columns[2:]
        
        # Group every 4 columns as one conversation
        conv_num = 1
        for i in range(0, len(cols), 4):
            if i+3 < len(cols):
                conv_data = {
                    'conversation_number': conv_num,
                    'emotional_reactions': convert_rating(row[cols[i]]),
                    'explorations': convert_rating(row[cols[i+1]]),
                    'interpretations': convert_rating(row[cols[i+2]]),
                    'empathy': convert_rating(row[cols[i+3]])
                }
                evaluator_data['conversations'].append(conv_data)
                conv_num += 1
        
        evaluators.append(evaluator_data)
    
    return evaluators

def convert_rating(rating_str):
    """Convert rating string to numeric value"""
    if pd.isna(rating_str):
        return None
    if '0' in str(rating_str):
        return 0
    elif '1' in str(rating_str):
        return 1
    elif '2' in str(rating_str):
        return 2
    return None

def load_llm_evaluations(metadata_csv):
    """Load LLM evaluation scores from metadata CSV"""
    df = pd.read_csv(metadata_csv)
    
    llm_scores = []
    for idx, row in df.iterrows():
        llm_scores.append({
            'conversation_index': row['index'],
            'participant_id': row['participant_id'],
            'session': row['session'],
            'round': row['round'],
            'emotional_reactions': row['emotional_reactions'],
            'explorations': row['explorations'],
            'interpretations': row['interpretations'],
            'empathy': row['empathy']
        })
    
    return llm_scores

def calculate_agreement_metrics(human_evals, llm_scores):
    """Calculate absolute agreement and correlations"""
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    # Prepare data for analysis
    comparison_data = {dim: {'human': [], 'llm': []} for dim in dimensions}
    
    # For each conversation in LLM scores
    for conv_idx, llm_conv in enumerate(llm_scores):
        conv_num = conv_idx + 1  # Conversation numbers are 1-indexed
        
        # Get all human ratings for this conversation
        for evaluator in human_evals:
            if conv_num <= len(evaluator['conversations']):
                human_conv = evaluator['conversations'][conv_num - 1]
                
                for dim in dimensions:
                    if human_conv[dim] is not None:
                        comparison_data[dim]['human'].append(human_conv[dim])
                        comparison_data[dim]['llm'].append(llm_conv[dim])
    
    # Calculate metrics
    results = {}
    
    for dim in dimensions:
        human_scores = np.array(comparison_data[dim]['human'])
        llm_scores = np.array(comparison_data[dim]['llm'])
        
        if len(human_scores) > 0:
            # Absolute agreement rate
            agreement_rate = np.mean(human_scores == llm_scores)
            
            # Spearman correlation
            spearman_corr, spearman_p = stats.spearmanr(human_scores, llm_scores)
            
            # Pearson correlation (for comparison)
            pearson_corr, pearson_p = stats.pearsonr(human_scores, llm_scores)
            
            # Within-one agreement (allows difference of 1)
            within_one = np.mean(np.abs(human_scores - llm_scores) <= 1)
            
            results[dim] = {
                'absolute_agreement': agreement_rate,
                'within_one_agreement': within_one,
                'spearman_correlation': spearman_corr,
                'spearman_p_value': spearman_p,
                'pearson_correlation': pearson_corr,
                'pearson_p_value': pearson_p,
                'n_comparisons': len(human_scores),
                'human_scores': human_scores,
                'llm_scores': llm_scores
            }
    
    return results

def calculate_inter_rater_reliability(human_evals):
    """Calculate inter-rater reliability among human evaluators using Krippendorff's alpha"""
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    # Get number of conversations
    n_conversations = len(human_evals[0]['conversations']) if human_evals else 0
    
    irr_results = {}
    
    for dim in dimensions:
        # Create matrix of ratings: rows = evaluators, columns = conversations
        ratings_matrix = []
        
        for evaluator in human_evals:
            evaluator_ratings = []
            for conv in evaluator['conversations']:
                if conv[dim] is not None:
                    evaluator_ratings.append(conv[dim])
                else:
                    evaluator_ratings.append(np.nan)
            ratings_matrix.append(evaluator_ratings)
        
        ratings_matrix = np.array(ratings_matrix)
        
        # Calculate Krippendorff's alpha
        # The krippendorff package expects data in the shape (raters, items)
        # Our ratings_matrix is already in this format
        try:
            # Calculate alpha for ordinal data (since empathy scores are 0, 1, 2)
            alpha = krippendorff.alpha(reliability_data=ratings_matrix, 
                                      level_of_measurement='ordinal')
        except:
            alpha = np.nan
        
        # Also calculate average pairwise agreement for comparison
        n_raters = len(ratings_matrix)
        
        if n_raters > 1:
            pairwise_agreements = []
            for i in range(n_raters):
                for j in range(i+1, n_raters):
                    mask = ~(np.isnan(ratings_matrix[i]) | np.isnan(ratings_matrix[j]))
                    if np.sum(mask) > 0:
                        agreement = np.mean(ratings_matrix[i][mask] == ratings_matrix[j][mask])
                        pairwise_agreements.append(agreement)
            
            avg_agreement = np.mean(pairwise_agreements) if pairwise_agreements else 0
            
            # Calculate percentage of perfect agreement across all raters
            perfect_agreement_count = 0
            total_items = 0
            for col_idx in range(ratings_matrix.shape[1]):
                col_data = ratings_matrix[:, col_idx]
                valid_ratings = col_data[~np.isnan(col_data)]
                if len(valid_ratings) > 1:
                    if len(np.unique(valid_ratings)) == 1:
                        perfect_agreement_count += 1
                    total_items += 1
            
            perfect_agreement_pct = (perfect_agreement_count / total_items * 100) if total_items > 0 else 0
            
            irr_results[dim] = {
                'krippendorff_alpha': alpha,
                'average_pairwise_agreement': avg_agreement,
                'perfect_agreement_pct': perfect_agreement_pct,
                'n_raters': n_raters,
                'n_conversations': n_conversations
            }
    
    return irr_results

def plot_agreement_analysis(results):
    """Create visualizations for agreement analysis"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    dimensions = list(results.keys())
    
    # Plot 1: Agreement rates comparison
    ax = axes[0, 0]
    agreement_types = ['Absolute\nAgreement', 'Within-One\nAgreement']
    x = np.arange(len(dimensions))
    width = 0.35
    
    abs_agreements = [results[d]['absolute_agreement'] for d in dimensions]
    within_one = [results[d]['within_one_agreement'] for d in dimensions]
    
    ax.bar(x - width/2, abs_agreements, width, label='Absolute', color='steelblue')
    ax.bar(x + width/2, within_one, width, label='Within ±1', color='lightcoral')
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Agreement Rate')
    ax.set_title('LLM-Human Agreement Rates')
    ax.set_xticks(x)
    ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions], rotation=0)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1])
    
    # Plot 2: Correlations
    ax = axes[0, 1]
    spearman_corrs = [results[d]['spearman_correlation'] for d in dimensions]
    pearson_corrs = [results[d]['pearson_correlation'] for d in dimensions]
    
    ax.bar(x - width/2, spearman_corrs, width, label='Spearman', color='darkgreen')
    ax.bar(x + width/2, pearson_corrs, width, label='Pearson', color='darkblue')
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Correlation Coefficient')
    ax.set_title('LLM-Human Correlations')
    ax.set_xticks(x)
    ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions], rotation=0)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1])
    
    # Plot 3: Summary metrics table
    ax = axes[0, 2]
    ax.axis('tight')
    ax.axis('off')
    
    table_data = []
    table_data.append(['Dimension', 'Abs Agree', 'Spearman ρ', 'p-value'])
    for dim in dimensions:
        table_data.append([
            dim.replace('_', ' ').title(),
            f"{results[dim]['absolute_agreement']:.3f}",
            f"{results[dim]['spearman_correlation']:.3f}",
            f"{results[dim]['spearman_p_value']:.4f}"
        ])
    
    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    
    # Header row styling
    for i in range(len(table_data[0])):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    ax.set_title('Summary Statistics', fontweight='bold', pad=20)
    
    # Plots 4-7: Scatter plots for each dimension
    for idx, dim in enumerate(dimensions):
        ax = axes[1, idx] if idx < 3 else axes[1, 2]
        
        if idx < 3:  # Only plot first 3 dimensions due to space
            human = results[dim]['human_scores']
            llm = results[dim]['llm_scores']
            
            # Add jitter for better visualization
            human_jitter = human + np.random.normal(0, 0.05, len(human))
            llm_jitter = llm + np.random.normal(0, 0.05, len(llm))
            
            ax.scatter(llm_jitter, human_jitter, alpha=0.5, s=30)
            
            # Add diagonal line for perfect agreement
            ax.plot([0, 2], [0, 2], 'r--', alpha=0.5, label='Perfect Agreement')
            
            # Add regression line
            z = np.polyfit(llm, human, 1)
            p = np.poly1d(z)
            ax.plot([0, 2], p([0, 2]), "b-", alpha=0.5, label='Trend')
            
            ax.set_xlabel('LLM Score')
            ax.set_ylabel('Human Score')
            ax.set_title(f'{dim.replace("_", " ").title()}')
            ax.set_xlim(-0.5, 2.5)
            ax.set_ylim(-0.5, 2.5)
            ax.set_xticks([0, 1, 2])
            ax.set_yticks([0, 1, 2])
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=8)
    
    plt.suptitle('LLM-Human Agreement Analysis for Empathy Evaluation', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    return fig

def print_detailed_report(results, irr_results):
    """Print detailed analysis report"""
    print("=" * 80)
    print("LLM-HUMAN AGREEMENT ANALYSIS REPORT")
    print("=" * 80)
    
    print("\n1. ABSOLUTE AGREEMENT RATES")
    print("-" * 40)
    for dim in results:
        print(f"\n{dim.replace('_', ' ').title()}:")
        print(f"  Absolute Agreement: {results[dim]['absolute_agreement']:.1%}")
        print(f"  Within-One Agreement: {results[dim]['within_one_agreement']:.1%}")
        print(f"  Number of Comparisons: {results[dim]['n_comparisons']}")
    
    print("\n2. CORRELATION ANALYSIS")
    print("-" * 40)
    for dim in results:
        print(f"\n{dim.replace('_', ' ').title()}:")
        print(f"  Spearman's ρ: {results[dim]['spearman_correlation']:.3f} (p={results[dim]['spearman_p_value']:.4f})")
        print(f"  Pearson's r: {results[dim]['pearson_correlation']:.3f} (p={results[dim]['pearson_p_value']:.4f})")
        
        # Interpret correlation strength
        rho = abs(results[dim]['spearman_correlation'])
        if rho >= 0.7:
            strength = "Strong"
        elif rho >= 0.5:
            strength = "Moderate"
        elif rho >= 0.3:
            strength = "Weak"
        else:
            strength = "Very Weak"
        print(f"  Correlation Strength: {strength}")
    
    print("\n3. INTER-RATER RELIABILITY (HUMAN EVALUATORS)")
    print("-" * 40)
    for dim in irr_results:
        print(f"\n{dim.replace('_', ' ').title()}:")
        print(f"  Krippendorff's α: {irr_results[dim]['krippendorff_alpha']:.3f}")
        print(f"  Average Pairwise Agreement: {irr_results[dim]['average_pairwise_agreement']:.1%}")
        print(f"  Perfect Agreement: {irr_results[dim]['perfect_agreement_pct']:.1f}% of conversations")
        print(f"  Number of Raters: {irr_results[dim]['n_raters']}")
        
        # Interpret Krippendorff's alpha
        alpha = irr_results[dim]['krippendorff_alpha']
        if alpha >= 0.8:
            reliability = "Good reliability"
        elif alpha >= 0.667:
            reliability = "Tentative reliability"
        else:
            reliability = "Low reliability"
        print(f"  Interpretation: {reliability}")
    
    print("\n4. OVERALL SUMMARY")
    print("-" * 40)
    
    # Calculate overall metrics
    avg_absolute = np.mean([results[d]['absolute_agreement'] for d in results])
    avg_within_one = np.mean([results[d]['within_one_agreement'] for d in results])
    avg_spearman = np.mean([results[d]['spearman_correlation'] for d in results])
    avg_human_agreement = np.mean([irr_results[d]['average_pairwise_agreement'] for d in irr_results])
    avg_krippendorff = np.mean([irr_results[d]['krippendorff_alpha'] for d in irr_results])
    
    print(f"\nAverage Absolute Agreement (LLM-Human): {avg_absolute:.1%}")
    print(f"Average Within-One Agreement (LLM-Human): {avg_within_one:.1%}")
    print(f"Average Spearman Correlation (LLM-Human): {avg_spearman:.3f}")
    print(f"Average Human Inter-Rater Agreement: {avg_human_agreement:.1%}")
    print(f"Average Krippendorff's α (Human IRR): {avg_krippendorff:.3f}")
    
    print("\n5. INTERPRETATION")
    print("-" * 40)
    
    if avg_spearman >= 0.7:
        print("✓ Strong correlation between LLM and human judgments")
    elif avg_spearman >= 0.5:
        print("✓ Moderate correlation between LLM and human judgments")
    else:
        print("⚠ Weak to moderate correlation between LLM and human judgments")
    
    if avg_absolute >= 0.7:
        print("✓ High absolute agreement rate")
    elif avg_absolute >= 0.5:
        print("✓ Moderate absolute agreement rate")
    else:
        print("⚠ Low to moderate absolute agreement rate")
    
    if avg_within_one >= 0.9:
        print("✓ Excellent within-one agreement (ratings rarely differ by more than 1)")
    elif avg_within_one >= 0.8:
        print("✓ Good within-one agreement")
    else:
        print("⚠ Moderate within-one agreement")
    
    if avg_krippendorff >= 0.8:
        print("✓ Good inter-rater reliability among human evaluators")
    elif avg_krippendorff >= 0.667:
        print("⚠ Tentative inter-rater reliability among human evaluators")
    else:
        print("⚠ Low inter-rater reliability among human evaluators")
    
    print("\n" + "=" * 80)

def main():
    """Main analysis function"""
    
    # File paths
    human_eval_path = "data/Empathy Evaluation - Set 1.csv"
    llm_metadata_path = "../google_forms/updated/conversation_set1_metadata.csv"
    
    print("Loading data...")
    
    # Load human evaluations
    human_evals = load_human_evaluations(human_eval_path)
    print(f"Loaded {len(human_evals)} human evaluators")
    
    # Load LLM evaluations
    llm_scores = load_llm_evaluations(llm_metadata_path)
    print(f"Loaded {len(llm_scores)} LLM-evaluated conversations")
    
    # Calculate agreement metrics
    print("\nCalculating agreement metrics...")
    results = calculate_agreement_metrics(human_evals, llm_scores)
    
    # Calculate inter-rater reliability
    print("Calculating inter-rater reliability...")
    irr_results = calculate_inter_rater_reliability(human_evals)
    
    # Print detailed report
    print_detailed_report(results, irr_results)
    
    # Create visualizations
    print("\nGenerating visualizations...")
    fig = plot_agreement_analysis(results)
    plt.savefig('llm_human_agreement_analysis.png', dpi=300, bbox_inches='tight')
    print("Saved visualization to llm_human_agreement_analysis.png")
    
    # Save results to CSV
    summary_df = pd.DataFrame({
        'Dimension': list(results.keys()),
        'Absolute_Agreement': [results[d]['absolute_agreement'] for d in results],
        'Within_One_Agreement': [results[d]['within_one_agreement'] for d in results],
        'Spearman_Correlation': [results[d]['spearman_correlation'] for d in results],
        'Spearman_P_Value': [results[d]['spearman_p_value'] for d in results],
        'Pearson_Correlation': [results[d]['pearson_correlation'] for d in results],
        'Pearson_P_Value': [results[d]['pearson_p_value'] for d in results],
        'N_Comparisons': [results[d]['n_comparisons'] for d in results],
        'Krippendorff_Alpha': [irr_results[d]['krippendorff_alpha'] for d in irr_results],
        'Human_Pairwise_Agreement': [irr_results[d]['average_pairwise_agreement'] for d in irr_results],
        'Perfect_Agreement_Pct': [irr_results[d]['perfect_agreement_pct'] for d in irr_results]
    })
    
    summary_df.to_csv('llm_human_agreement_summary.csv', index=False)
    print("Saved summary statistics to llm_human_agreement_summary.csv")
    
    plt.show()

if __name__ == "__main__":
    main()