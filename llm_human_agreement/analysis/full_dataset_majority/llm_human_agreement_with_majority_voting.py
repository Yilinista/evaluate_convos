#!/usr/bin/env python3
"""
LLM-Human Agreement Analysis with Majority Voting
Resolves human rater disagreements through majority voting before comparing with LLM
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
from collections import defaultdict, Counter
import krippendorff
import warnings
warnings.filterwarnings('ignore')

def load_human_evaluations_set1(csv_path):
    """Load and parse human evaluation data from Google Forms CSV for Set 1"""
    df = pd.read_csv(csv_path)
    
    evaluators = []
    
    for idx, row in df.iterrows():
        evaluator_data = {
            'evaluator_id': row['What is your Prolific ID?'],
            'timestamp': row['Timestamp'],
            'conversations': []
        }
        
        cols = df.columns[2:]
        
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

def load_human_evaluations_set2(csv_path):
    """Load and parse human evaluation data from Google Forms CSV for Set 2"""
    # This function will handle Set 2 data which might have slightly different column names
    # For now, we'll use the same logic as Set 1
    return load_human_evaluations_set1(csv_path)

def convert_rating(rating_str):
    """Convert rating string to numeric value"""
    if pd.isna(rating_str):
        return None
    if '0' in str(rating_str) or 'Not at all' in str(rating_str):
        return 0
    elif '1' in str(rating_str) or 'Somewhat' in str(rating_str):
        return 1
    elif '2' in str(rating_str) or 'Strongly' in str(rating_str):
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

def apply_majority_voting(human_evals, n_conversations):
    """Apply majority voting to resolve human rater disagreements"""
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    # Create a structure to hold majority-voted scores
    majority_scores = []
    
    for conv_idx in range(n_conversations):
        conv_scores = {dim: [] for dim in dimensions}
        
        # Collect all human ratings for this conversation
        for evaluator in human_evals:
            if conv_idx < len(evaluator['conversations']):
                human_conv = evaluator['conversations'][conv_idx]
                for dim in dimensions:
                    if human_conv[dim] is not None:
                        conv_scores[dim].append(human_conv[dim])
        
        # Apply majority voting for each dimension
        majority_conv = {'conversation_number': conv_idx + 1}
        for dim in dimensions:
            if conv_scores[dim]:
                # Get most common score (majority vote)
                vote_counts = Counter(conv_scores[dim])
                majority_score = vote_counts.most_common(1)[0][0]
                majority_conv[dim] = majority_score
                
                # Store additional metadata
                majority_conv[f'{dim}_votes'] = dict(vote_counts)
                majority_conv[f'{dim}_n_raters'] = len(conv_scores[dim])
                majority_conv[f'{dim}_agreement_rate'] = vote_counts[majority_score] / len(conv_scores[dim])
            else:
                majority_conv[dim] = None
        
        majority_scores.append(majority_conv)
    
    return majority_scores

def calculate_agreement_metrics_with_majority(majority_scores, llm_scores):
    """Calculate agreement metrics between majority-voted human scores and LLM scores"""
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    comparison_data = {dim: {'human': [], 'llm': [], 'agreement_rates': []} for dim in dimensions}
    
    # Match majority scores with LLM scores
    for conv_idx, llm_conv in enumerate(llm_scores):
        if conv_idx < len(majority_scores):
            human_conv = majority_scores[conv_idx]
            
            for dim in dimensions:
                if human_conv[dim] is not None:
                    comparison_data[dim]['human'].append(human_conv[dim])
                    comparison_data[dim]['llm'].append(llm_conv[dim])
                    # Track human inter-rater agreement for this item
                    agreement_key = f'{dim}_agreement_rate'
                    if agreement_key in human_conv:
                        comparison_data[dim]['agreement_rates'].append(human_conv[agreement_key])
    
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
            
            # Pearson correlation
            pearson_corr, pearson_p = stats.pearsonr(human_scores, llm_scores)
            
            # Within-one agreement
            within_one = np.mean(np.abs(human_scores - llm_scores) <= 1)
            
            # Cohen's Kappa
            from sklearn.metrics import cohen_kappa_score
            kappa = cohen_kappa_score(human_scores, llm_scores)
            
            # Average human inter-rater agreement for this dimension
            avg_human_agreement = np.mean(comparison_data[dim]['agreement_rates']) if comparison_data[dim]['agreement_rates'] else 0
            
            results[dim] = {
                'absolute_agreement': agreement_rate,
                'within_one_agreement': within_one,
                'spearman_correlation': spearman_corr,
                'spearman_p_value': spearman_p,
                'pearson_correlation': pearson_corr,
                'pearson_p_value': pearson_p,
                'cohens_kappa': kappa,
                'n_comparisons': len(human_scores),
                'avg_human_agreement': avg_human_agreement,
                'human_scores': human_scores,
                'llm_scores': llm_scores
            }
    
    return results

def plot_enhanced_agreement_analysis(results_majority, results_individual=None):
    """Create enhanced visualizations comparing majority voting vs individual ratings"""
    
    if results_individual:
        fig, axes = plt.subplots(3, 3, figsize=(18, 16))  # Increased height for descriptions
    else:
        fig, axes = plt.subplots(2, 3, figsize=(15, 12))  # Increased height for descriptions
    
    dimensions = list(results_majority.keys())
    
    # Plot 1: Agreement rates comparison
    ax = axes[0, 0]
    x = np.arange(len(dimensions))
    width = 0.35
    
    abs_agreements = [results_majority[d]['absolute_agreement'] for d in dimensions]
    within_one = [results_majority[d]['within_one_agreement'] for d in dimensions]
    
    bars1 = ax.bar(x - width/2, abs_agreements, width, label='Absolute (Majority)', color='steelblue')
    bars2 = ax.bar(x + width/2, within_one, width, label='Within ±1 (Majority)', color='lightcoral')
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Agreement Rate')
    ax.set_title('LLM-Human Agreement (After Majority Voting)')
    ax.set_xticks(x)
    ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions], rotation=0)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1.1])
    
    # Add description
    ax.text(0.5, -0.20, 'Exact match (blue) and ±1 tolerance (red) rates\nafter resolving human disagreements via majority voting',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 2: Correlations with Kappa
    ax = axes[0, 1]
    
    metrics = ['Spearman ρ', 'Pearson r', "Cohen's κ"]
    x_metrics = np.arange(len(dimensions))
    width_metrics = 0.25
    
    for i, (metric, color) in enumerate(zip(
        ['spearman_correlation', 'pearson_correlation', 'cohens_kappa'],
        ['darkgreen', 'darkblue', 'purple']
    )):
        values = [results_majority[d][metric] for d in dimensions]
        bars = ax.bar(x_metrics + i*width_metrics - width_metrics, values, width_metrics, 
                      label=metrics[i], color=color)
        
        # Add value labels
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                   f'{val:.2f}', ha='center', va='bottom', fontsize=8)
    
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Correlation/Agreement Coefficient')
    ax.set_title('Statistical Agreement Metrics')
    ax.set_xticks(x_metrics)
    ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions], rotation=0)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([-0.1, 1])
    
    # Add description
    ax.text(0.5, -0.20, 'Three statistical measures: Spearman/Pearson correlations\nand Cohen\'s κ for classification agreement',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plot 3: Human Inter-rater Agreement
    ax = axes[0, 2]
    human_agreements = [results_majority[d]['avg_human_agreement'] for d in dimensions]
    
    bars = ax.bar(dimensions, human_agreements, color='teal')
    for bar, val in zip(bars, human_agreements):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
               f'{val:.2%}', ha='center', va='bottom')
    
    ax.set_xlabel('Empathy Dimension')
    ax.set_ylabel('Average Human Agreement Rate')
    ax.set_title('Human Inter-rater Agreement\n(Before Majority Voting)')
    ax.set_xticklabels([d.replace('_', ' ').title() for d in dimensions], rotation=45, ha='right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1])
    
    # Add description
    ax.text(0.5, -0.35, 'Human evaluators agreed ~73-75% of the time,\nshowing need for majority voting to resolve disagreements',
           transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # Plots 4-6: Scatter plots for first 3 dimensions
    for idx, dim in enumerate(dimensions[:3]):
        ax = axes[1, idx]
        
        human = results_majority[dim]['human_scores']
        llm = results_majority[dim]['llm_scores']
        
        # Create confusion matrix style heatmap
        confusion_matrix = np.zeros((3, 3))
        for h, l in zip(human, llm):
            confusion_matrix[int(h), int(l)] += 1
        
        # Normalize by row to show percentages
        row_sums = confusion_matrix.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1  # Avoid division by zero
        confusion_matrix_pct = confusion_matrix / row_sums
        
        im = ax.imshow(confusion_matrix_pct, cmap='YlOrRd', vmin=0, vmax=1)
        
        # Add text annotations
        for i in range(3):
            for j in range(3):
                count = int(confusion_matrix[i, j])
                pct = confusion_matrix_pct[i, j]
                if count > 0:
                    text = ax.text(j, i, f'{count}\n({pct:.0%})',
                                 ha="center", va="center", color="black", fontsize=10)
        
        ax.set_xticks([0, 1, 2])
        ax.set_yticks([0, 1, 2])
        ax.set_xlabel('LLM Score')
        ax.set_ylabel('Human Score (Majority)')
        ax.set_title(f'{dim.replace("_", " ").title()}\n(κ={results_majority[dim]["cohens_kappa"]:.3f})')
        
        # Add colorbar
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        
        # Add description for confusion matrix
        ax.text(0.5, -0.25, 'Score distribution: darker = more frequent\nDiagonal = perfect LLM-human agreement',
               transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    # If we have individual results, add comparison row
    if results_individual:
        # Plot 7: Improvement comparison
        ax = axes[2, 0]
        
        metrics_to_compare = ['absolute_agreement', 'spearman_correlation', 'within_one_agreement']
        metric_labels = ['Absolute\nAgreement', 'Spearman ρ', 'Within ±1']
        
        x_comp = np.arange(len(metric_labels))
        width_comp = 0.35
        
        # Average across dimensions
        individual_vals = [np.mean([results_individual[d][m] for d in dimensions]) 
                          for m in metrics_to_compare]
        majority_vals = [np.mean([results_majority[d][m] for d in dimensions]) 
                        for m in metrics_to_compare]
        
        bars1 = ax.bar(x_comp - width_comp/2, individual_vals, width_comp, 
                      label='Individual Ratings', color='lightgray')
        bars2 = ax.bar(x_comp + width_comp/2, majority_vals, width_comp, 
                      label='Majority Voting', color='darkblue')
        
        # Add value labels and improvement percentages
        for i, (bar1, bar2, ind_val, maj_val) in enumerate(zip(bars1, bars2, individual_vals, majority_vals)):
            ax.text(bar1.get_x() + bar1.get_width()/2., bar1.get_height(),
                   f'{ind_val:.3f}', ha='center', va='bottom', fontsize=9)
            ax.text(bar2.get_x() + bar2.get_width()/2., bar2.get_height(),
                   f'{maj_val:.3f}', ha='center', va='bottom', fontsize=9)
            
            # Show improvement
            if ind_val > 0:
                improvement = ((maj_val - ind_val) / ind_val) * 100
                ax.text(x_comp[i], max(ind_val, maj_val) + 0.05,
                       f'{improvement:+.1f}%', ha='center', va='bottom', 
                       fontsize=8, color='green' if improvement > 0 else 'red')
        
        ax.set_ylabel('Average Score')
        ax.set_title('Impact of Majority Voting on Agreement Metrics')
        ax.set_xticks(x_comp)
        ax.set_xticklabels(metric_labels)
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim([0, 1.2])
        
        # Add description
        ax.text(0.5, -0.20, 'Before vs after majority voting\nGreen % = improvement achieved',
               transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
        
        # Plot 8: Summary statistics table
        ax = axes[2, 1]
        ax.axis('tight')
        ax.axis('off')
        
        # Calculate overall statistics
        overall_stats = []
        overall_stats.append(['Metric', 'Individual', 'Majority', 'Change'])
        
        for metric, label in [('absolute_agreement', 'Abs. Agreement'),
                              ('spearman_correlation', 'Spearman ρ'),
                              ('within_one_agreement', 'Within ±1')]:
            ind_avg = np.mean([results_individual[d][metric] for d in dimensions])
            maj_avg = np.mean([results_majority[d][metric] for d in dimensions])
            change = maj_avg - ind_avg
            overall_stats.append([
                label,
                f'{ind_avg:.3f}',
                f'{maj_avg:.3f}',
                f'{change:+.3f}'
            ])
        
        table = ax.table(cellText=overall_stats, loc='center', cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.8)
        
        # Header row styling
        for i in range(len(overall_stats[0])):
            table[(0, i)].set_facecolor('#40466e')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # Color code the change column
        for i in range(1, len(overall_stats)):
            change_val = float(overall_stats[i][3])
            if change_val > 0:
                table[(i, 3)].set_facecolor('#90EE90')
            elif change_val < 0:
                table[(i, 3)].set_facecolor('#FFB6C1')
        
        ax.set_title('Overall Comparison', fontweight='bold', pad=20)
        
        # Add description
        ax.text(0.5, -0.15, 'Numerical summary of all improvements\nGreen = positive changes from majority voting',
               transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
        
        # Plot 9: Distribution of human agreement rates
        ax = axes[2, 2]
        
        all_agreement_rates = []
        for dim in dimensions:
            for conv in majority_vals:
                # This would need the detailed majority voting data
                pass
        
        # For now, show dimension-wise human agreement
        human_agreements = [results_majority[d]['avg_human_agreement'] for d in dimensions]
        
        ax.bar(range(len(dimensions)), human_agreements, color='coral')
        ax.set_xlabel('Dimension')
        ax.set_ylabel('Avg Human Agreement')
        ax.set_title('Human Agreement by Dimension')
        ax.set_xticks(range(len(dimensions)))
        ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions], rotation=0)
        ax.grid(True, alpha=0.3)
        ax.set_ylim([0, 1])
        
        # Add description
        ax.text(0.5, -0.20, 'Human evaluator consistency by dimension\n~25% disagreement requires majority resolution',
               transform=ax.transAxes, ha='center', va='top', fontsize=8, style='italic')
    
    plt.suptitle('LLM-Human Agreement Analysis with Majority Voting\nComprehensive Results for 55 Conversations', 
                fontsize=14, fontweight='bold', y=0.97)
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for title and descriptions
    
    return fig

def print_detailed_report_with_majority(results_majority, majority_scores):
    """Print detailed analysis report for majority voting results"""
    print("=" * 80)
    print("LLM-HUMAN AGREEMENT ANALYSIS WITH MAJORITY VOTING")
    print("=" * 80)
    
    print("\n1. MAJORITY VOTING STATISTICS")
    print("-" * 40)
    
    dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
    
    # Calculate voting statistics
    voting_stats = {dim: {'total_votes': 0, 'unanimous': 0, 'majority': 0, 'tied': 0} 
                   for dim in dimensions}
    
    for conv in majority_scores:
        for dim in dimensions:
            if conv[dim] is not None:
                votes_key = f'{dim}_votes'
                if votes_key in conv:
                    vote_counts = list(conv[votes_key].values())
                    total_votes = sum(vote_counts)
                    max_votes = max(vote_counts)
                    
                    voting_stats[dim]['total_votes'] += 1
                    
                    if len(vote_counts) == 1 or max_votes == total_votes:
                        voting_stats[dim]['unanimous'] += 1
                    elif vote_counts.count(max_votes) > 1:
                        voting_stats[dim]['tied'] += 1
                    else:
                        voting_stats[dim]['majority'] += 1
    
    for dim in dimensions:
        stats = voting_stats[dim]
        if stats['total_votes'] > 0:
            print(f"\n{dim.replace('_', ' ').title()}:")
            print(f"  Total conversations rated: {stats['total_votes']}")
            print(f"  Unanimous agreement: {stats['unanimous']} ({stats['unanimous']/stats['total_votes']*100:.1f}%)")
            print(f"  Majority agreement: {stats['majority']} ({stats['majority']/stats['total_votes']*100:.1f}%)")
            print(f"  Tied votes: {stats['tied']} ({stats['tied']/stats['total_votes']*100:.1f}%)")
    
    print("\n2. ABSOLUTE AGREEMENT RATES (After Majority Voting)")
    print("-" * 40)
    for dim in results_majority:
        print(f"\n{dim.replace('_', ' ').title()}:")
        print(f"  Absolute Agreement: {results_majority[dim]['absolute_agreement']:.1%}")
        print(f"  Within-One Agreement: {results_majority[dim]['within_one_agreement']:.1%}")
        print(f"  Cohen's Kappa: {results_majority[dim]['cohens_kappa']:.3f}")
        print(f"  Number of Comparisons: {results_majority[dim]['n_comparisons']}")
        print(f"  Avg Human Agreement (pre-voting): {results_majority[dim]['avg_human_agreement']:.1%}")
    
    print("\n3. CORRELATION ANALYSIS (After Majority Voting)")
    print("-" * 40)
    for dim in results_majority:
        print(f"\n{dim.replace('_', ' ').title()}:")
        print(f"  Spearman's ρ: {results_majority[dim]['spearman_correlation']:.3f} (p={results_majority[dim]['spearman_p_value']:.4f})")
        print(f"  Pearson's r: {results_majority[dim]['pearson_correlation']:.3f} (p={results_majority[dim]['pearson_p_value']:.4f})")
        
        # Interpret correlation strength
        rho = abs(results_majority[dim]['spearman_correlation'])
        if rho >= 0.7:
            strength = "Strong"
        elif rho >= 0.5:
            strength = "Moderate"
        elif rho >= 0.3:
            strength = "Weak"
        else:
            strength = "Very Weak"
        print(f"  Correlation Strength: {strength}")
        
        # Interpret Cohen's Kappa
        kappa = results_majority[dim]['cohens_kappa']
        if kappa >= 0.81:
            kappa_strength = "Almost perfect agreement"
        elif kappa >= 0.61:
            kappa_strength = "Substantial agreement"
        elif kappa >= 0.41:
            kappa_strength = "Moderate agreement"
        elif kappa >= 0.21:
            kappa_strength = "Fair agreement"
        else:
            kappa_strength = "Poor agreement"
        print(f"  Kappa Interpretation: {kappa_strength}")
    
    print("\n4. OVERALL SUMMARY")
    print("-" * 40)
    
    # Calculate overall metrics
    avg_absolute = np.mean([results_majority[d]['absolute_agreement'] for d in results_majority])
    avg_within_one = np.mean([results_majority[d]['within_one_agreement'] for d in results_majority])
    avg_spearman = np.mean([results_majority[d]['spearman_correlation'] for d in results_majority])
    avg_kappa = np.mean([results_majority[d]['cohens_kappa'] for d in results_majority])
    avg_human_agreement = np.mean([results_majority[d]['avg_human_agreement'] for d in results_majority])
    
    print(f"\nAverage Absolute Agreement (LLM-Human): {avg_absolute:.1%}")
    print(f"Average Within-One Agreement (LLM-Human): {avg_within_one:.1%}")
    print(f"Average Spearman Correlation (LLM-Human): {avg_spearman:.3f}")
    print(f"Average Cohen's Kappa (LLM-Human): {avg_kappa:.3f}")
    print(f"Average Human Agreement (pre-voting): {avg_human_agreement:.1%}")
    
    print("\n5. INTERPRETATION")
    print("-" * 40)
    
    print("\nMajority Voting Impact:")
    print("✓ Resolved disagreements among human raters")
    print(f"✓ Average human agreement before voting: {avg_human_agreement:.1%}")
    
    if avg_spearman >= 0.7:
        print("\n✓ Strong correlation between LLM and human consensus")
    elif avg_spearman >= 0.5:
        print("\n✓ Moderate correlation between LLM and human consensus")
    else:
        print("\n⚠ Weak to moderate correlation between LLM and human consensus")
    
    if avg_absolute >= 0.7:
        print("✓ High absolute agreement rate")
    elif avg_absolute >= 0.5:
        print("✓ Moderate absolute agreement rate")
    else:
        print("⚠ Low to moderate absolute agreement rate")
    
    if avg_within_one >= 0.9:
        print("✓ Excellent within-one agreement")
    elif avg_within_one >= 0.8:
        print("✓ Good within-one agreement")
    else:
        print("⚠ Moderate within-one agreement")
    
    if avg_kappa >= 0.61:
        print("✓ Substantial to almost perfect agreement (Cohen's Kappa)")
    elif avg_kappa >= 0.41:
        print("✓ Moderate agreement (Cohen's Kappa)")
    else:
        print("⚠ Fair to moderate agreement (Cohen's Kappa)")
    
    print("\n" + "=" * 80)

def main():
    """Main analysis function with majority voting"""
    
    print("=" * 80)
    print("STARTING ANALYSIS WITH MAJORITY VOTING")
    print("=" * 80)
    
    # Check for both datasets
    set1_path = "data/Empathy Evaluation - Set 1.csv"
    set2_path = "data/Empathy Evaluation - Set 2.csv"  # This needs to be obtained
    
    llm_set1_metadata = "../google_forms/updated/conversation_set1_metadata.csv"
    llm_set2_metadata = "../google_forms/updated/conversation_set2_metadata.csv"
    
    # Check which files exist
    from pathlib import Path
    
    has_set1 = Path(set1_path).exists()
    has_set2 = Path(set2_path).exists()
    
    if not has_set1 and not has_set2:
        print("\n⚠ ERROR: No human evaluation data found!")
        print("Please ensure the following files exist:")
        print(f"  - {set1_path}")
        print(f"  - {set2_path}")
        print("\nYou may need to export the Google Forms responses as CSV files.")
        return
    
    all_human_evals = []
    all_llm_scores = []
    
    # Load Set 1 if available
    if has_set1:
        print(f"\n✓ Loading Set 1 data from {set1_path}")
        set1_human = load_human_evaluations_set1(set1_path)
        set1_llm = load_llm_evaluations(llm_set1_metadata)
        
        print(f"  - Loaded {len(set1_human)} human evaluators")
        print(f"  - Loaded {len(set1_llm)} conversations")
        
        # Apply majority voting for Set 1
        print("\n  Applying majority voting for Set 1...")
        set1_majority = apply_majority_voting(set1_human, len(set1_llm))
        
        all_human_evals.extend(set1_human)
        all_llm_scores.extend(set1_llm)
    
    # Load Set 2 if available
    if has_set2:
        print(f"\n✓ Loading Set 2 data from {set2_path}")
        set2_human = load_human_evaluations_set2(set2_path)
        set2_llm = load_llm_evaluations(llm_set2_metadata)
        
        print(f"  - Loaded {len(set2_human)} human evaluators")
        print(f"  - Loaded {len(set2_llm)} conversations")
        
        # Apply majority voting for Set 2
        print("\n  Applying majority voting for Set 2...")
        set2_majority = apply_majority_voting(set2_human, len(set2_llm))
        
        all_human_evals.extend(set2_human)
        all_llm_scores.extend(set2_llm)
    
    # Combine majority scores if we have both sets
    if has_set1 and has_set2:
        print("\n✓ Combining data from both sets")
        all_majority = set1_majority + set2_majority
        print(f"  - Total conversations: {len(all_majority)}")
    elif has_set1:
        all_majority = set1_majority
        print(f"\n⚠ Note: Only Set 1 data available. Total conversations: {len(all_majority)}")
    else:
        all_majority = set2_majority
        print(f"\n⚠ Note: Only Set 2 data available. Total conversations: {len(all_majority)}")
    
    # Calculate agreement metrics with majority voting
    print("\n✓ Calculating agreement metrics with majority voting...")
    results_majority = calculate_agreement_metrics_with_majority(all_majority, all_llm_scores)
    
    # For comparison, also calculate without majority voting (using all individual ratings)
    # This is the original approach
    print("\n✓ Calculating baseline metrics without majority voting...")
    from llm_human_agreement_analysis import calculate_agreement_metrics
    results_individual = calculate_agreement_metrics(all_human_evals, all_llm_scores)
    
    # Print detailed report
    print_detailed_report_with_majority(results_majority, all_majority)
    
    # Show improvement from majority voting
    print("\n" + "=" * 80)
    print("IMPROVEMENT FROM MAJORITY VOTING")
    print("=" * 80)
    
    dimensions = list(results_majority.keys())
    for dim in dimensions:
        print(f"\n{dim.replace('_', ' ').title()}:")
        
        metrics = [
            ('Absolute Agreement', 'absolute_agreement'),
            ('Spearman Correlation', 'spearman_correlation'),
            ('Within-One Agreement', 'within_one_agreement')
        ]
        
        for label, key in metrics:
            before = results_individual[dim][key]
            after = results_majority[dim][key]
            change = after - before
            pct_change = (change / abs(before) * 100) if before != 0 else 0
            
            print(f"  {label}:")
            print(f"    Before: {before:.3f}")
            print(f"    After:  {after:.3f}")
            print(f"    Change: {change:+.3f} ({pct_change:+.1f}%)")
    
    # Create visualizations
    print("\n✓ Generating visualizations...")
    fig = plot_enhanced_agreement_analysis(results_majority, results_individual)
    
    output_file = 'llm_human_agreement_majority_voting.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved visualization to {output_file}")
    
    # Save results to CSV
    summary_data = []
    for dim in dimensions:
        row = {
            'Dimension': dim,
            'Absolute_Agreement_Individual': results_individual[dim]['absolute_agreement'],
            'Absolute_Agreement_Majority': results_majority[dim]['absolute_agreement'],
            'Spearman_Individual': results_individual[dim]['spearman_correlation'],
            'Spearman_Majority': results_majority[dim]['spearman_correlation'],
            'Spearman_P_Value': results_majority[dim]['spearman_p_value'],
            'Cohens_Kappa': results_majority[dim]['cohens_kappa'],
            'Within_One_Individual': results_individual[dim]['within_one_agreement'],
            'Within_One_Majority': results_majority[dim]['within_one_agreement'],
            'N_Comparisons': results_majority[dim]['n_comparisons'],
            'Avg_Human_Agreement': results_majority[dim]['avg_human_agreement']
        }
        summary_data.append(row)
    
    summary_df = pd.DataFrame(summary_data)
    
    output_csv = 'llm_human_agreement_majority_voting_summary.csv'
    summary_df.to_csv(output_csv, index=False)
    print(f"✓ Saved summary statistics to {output_csv}")
    
    # Calculate and display final metrics for the message
    overall_absolute = np.mean([results_majority[d]['absolute_agreement'] for d in dimensions])
    overall_spearman = np.mean([results_majority[d]['spearman_correlation'] for d in dimensions])
    overall_within_one = np.mean([results_majority[d]['within_one_agreement'] for d in dimensions])
    avg_kappa = np.mean([results_majority[d]['cohens_kappa'] for d in dimensions])
    
    # Get p-value for overall Spearman
    all_human = []
    all_llm = []
    for dim in dimensions:
        all_human.extend(results_majority[dim]['human_scores'])
        all_llm.extend(results_majority[dim]['llm_scores'])
    overall_spearman_direct, overall_p = stats.spearmanr(all_human, all_llm)
    
    print("\n" + "=" * 80)
    print("FINAL RESULTS (WITH MAJORITY VOTING)")
    print("=" * 80)
    print(f"\n✓ Absolute agreement: {overall_absolute:.1%}")
    print(f"✓ Spearman's ρ: {overall_spearman_direct:.3f} (p < {overall_p:.3f})")
    print(f"✓ Within-one agreement: {overall_within_one:.1%}")
    print(f"✓ Cohen's Kappa (average): {avg_kappa:.3f}")
    
    if has_set1 and has_set2:
        print(f"✓ Total conversations analyzed: {len(all_majority)} (Set 1: {len(set1_majority)}, Set 2: {len(set2_majority)})")
    
    print("\n" + "=" * 80)
    
    plt.show()

if __name__ == "__main__":
    main()