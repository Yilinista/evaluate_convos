"""
Post-Collection Analysis Pipeline for Empathy Evaluation Study

This script analyzes Google Forms responses comparing human and LLM empathy ratings.
Run this after collecting responses from Prolific study.

Requirements:
pip install pandas numpy scipy scikit-learn matplotlib seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import cohen_kappa_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

class EmpathyAnalysisPipeline:
    def __init__(self, responses_csv: str):
        """
        Initialize with Google Forms responses CSV.
        
        Args:
            responses_csv: Path to exported Google Forms responses
        """
        self.responses = pd.read_csv(responses_csv)
        self.dimensions = ['emotional_reactions', 'explorations', 'interpretations', 'empathy']
        self.setup_data()
        
    def setup_data(self):
        """Clean and prepare the data for analysis."""
        print("Setting up data...")
        
        # Map form column names to standard names
        # Adjust these based on your actual form column names
        column_mapping = {
            'Empathy Ratings - Conversation 1 [Emotional Reactions]': 'human_emotional_reactions_1',
            'Empathy Ratings - Conversation 1 [Explorations]': 'human_explorations_1',
            # Add more mappings based on your form structure
        }
        
        # Convert rating strings to numeric values
        rating_map = {'0 (Not at all)': 0, '1 (Somewhat)': 1, '2 (Strongly)': 2}
        
        # Clean and convert ratings
        for col in self.responses.columns:
            if any(rating in str(self.responses[col].iloc[0]) for rating in rating_map.keys()):
                self.responses[col] = self.responses[col].map(rating_map)
        
        print(f"Loaded {len(self.responses)} responses")
        
    def calculate_correlations(self):
        """Calculate correlations between LLM and human ratings."""
        print("\n" + "="*50)
        print("CORRELATION ANALYSIS")
        print("="*50)
        
        correlations = {}
        
        for dim in self.dimensions:
            # Extract LLM and human scores for this dimension across all conversations
            llm_scores = []
            human_scores = []
            
            # Collect scores from all conversations
            for conv_num in range(1, 31):  # Adjust based on your conversation count
                llm_col = f'llm_{dim}_{conv_num}'
                human_col = f'human_{dim}_{conv_num}'
                
                if llm_col in self.responses.columns and human_col in self.responses.columns:
                    llm_scores.extend(self.responses[llm_col].dropna().tolist())
                    human_scores.extend(self.responses[human_col].dropna().tolist())
            
            if len(llm_scores) > 0 and len(human_scores) > 0:
                # Pearson correlation
                pearson_r, pearson_p = pearsonr(llm_scores, human_scores)
                
                # Spearman correlation (rank-based)
                spearman_r, spearman_p = spearmanr(llm_scores, human_scores)
                
                correlations[dim] = {
                    'pearson_r': pearson_r,
                    'pearson_p': pearson_p,
                    'spearman_r': spearman_r, 
                    'spearman_p': spearman_p,
                    'n_pairs': len(llm_scores)
                }
                
                print(f"\n{dim.replace('_', ' ').title()}:")
                print(f"  Pearson r = {pearson_r:.3f} (p = {pearson_p:.3f})")
                print(f"  Spearman ρ = {spearman_r:.3f} (p = {spearman_p:.3f})")
                print(f"  Sample size: {len(llm_scores)} ratings")
                
        return correlations
    
    def calculate_agreement_metrics(self):
        """Calculate inter-rater agreement metrics."""
        print("\n" + "="*50)
        print("AGREEMENT ANALYSIS")  
        print("="*50)
        
        agreement_results = {}
        
        for dim in self.dimensions:
            llm_scores = []
            human_scores = []
            
            # Collect all score pairs
            for conv_num in range(1, 31):
                llm_col = f'llm_{dim}_{conv_num}'
                human_col = f'human_{dim}_{conv_num}'
                
                if llm_col in self.responses.columns and human_col in self.responses.columns:
                    valid_pairs = self.responses[[llm_col, human_col]].dropna()
                    llm_scores.extend(valid_pairs[llm_col].tolist())
                    human_scores.extend(valid_pairs[human_col].tolist())
            
            if len(llm_scores) > 0:
                # Cohen's Kappa
                kappa = cohen_kappa_score(llm_scores, human_scores)
                
                # Mean Absolute Error
                mae = mean_absolute_error(llm_scores, human_scores)
                
                # Exact agreement percentage
                exact_agreement = np.mean(np.array(llm_scores) == np.array(human_scores)) * 100
                
                # Within-1-point agreement
                within_one = np.mean(np.abs(np.array(llm_scores) - np.array(human_scores)) <= 1) * 100
                
                agreement_results[dim] = {
                    'kappa': kappa,
                    'mae': mae,
                    'exact_agreement': exact_agreement,
                    'within_one_agreement': within_one
                }
                
                print(f"\n{dim.replace('_', ' ').title()}:")
                print(f"  Cohen's κ = {kappa:.3f}")
                print(f"  Mean Absolute Error = {mae:.3f}")
                print(f"  Exact Agreement = {exact_agreement:.1f}%")
                print(f"  Within-1-Point Agreement = {within_one:.1f}%")
                
        return agreement_results
    
    def analyze_human_consistency(self):
        """Analyze consistency among human raters."""
        print("\n" + "="*50)
        print("HUMAN RATER CONSISTENCY")
        print("="*50)
        
        # Calculate standard deviation of human ratings for each conversation
        human_std_by_conversation = {}
        
        for conv_num in range(1, 31):
            conv_stds = {}
            for dim in self.dimensions:
                human_col = f'human_{dim}_{conv_num}'
                if human_col in self.responses.columns:
                    std_dev = self.responses[human_col].std()
                    conv_stds[dim] = std_dev
            
            if conv_stds:
                human_std_by_conversation[conv_num] = conv_stds
        
        # Calculate average consistency across conversations
        avg_consistency = {}
        for dim in self.dimensions:
            stds = [conv_stds.get(dim, np.nan) for conv_stds in human_std_by_conversation.values()]
            avg_consistency[dim] = np.nanmean(stds)
            print(f"{dim.replace('_', ' ').title()}: Avg SD = {avg_consistency[dim]:.3f}")
        
        return avg_consistency
    
    def create_visualizations(self, save_path: str = "empathy_analysis_charts.png"):
        """Create comprehensive visualization of results."""
        print(f"\nCreating visualizations...")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Empathy Evaluation: LLM vs Human Ratings Analysis', fontsize=16, fontweight='bold')
        
        # 1. Correlation heatmap
        correlation_data = []
        for dim in self.dimensions:
            llm_scores = []
            human_scores = []
            
            for conv_num in range(1, 31):
                llm_col = f'llm_{dim}_{conv_num}'
                human_col = f'human_{dim}_{conv_num}'
                
                if llm_col in self.responses.columns and human_col in self.responses.columns:
                    valid_pairs = self.responses[[llm_col, human_col]].dropna()
                    llm_scores.extend(valid_pairs[llm_col].tolist())
                    human_scores.extend(valid_pairs[human_col].tolist())
            
            if len(llm_scores) > 0:
                correlation_data.append({
                    'Dimension': dim.replace('_', ' ').title(),
                    'LLM_Scores': llm_scores,
                    'Human_Scores': human_scores
                })
        
        # Scatter plot for correlations
        ax1 = axes[0, 0]
        for i, data in enumerate(correlation_data):
            ax1.scatter(data['LLM_Scores'], data['Human_Scores'], 
                       alpha=0.6, label=data['Dimension'], s=30)
        
        ax1.set_xlabel('LLM Ratings')
        ax1.set_ylabel('Human Ratings')
        ax1.set_title('LLM vs Human Rating Correlations')
        ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # 2. Agreement by dimension
        ax2 = axes[0, 1]
        agreement_data = self.calculate_agreement_metrics()
        
        dimensions_clean = [dim.replace('_', ' ').title() for dim in self.dimensions]
        kappa_values = [agreement_data.get(dim, {}).get('kappa', 0) for dim in self.dimensions]
        
        bars = ax2.bar(dimensions_clean, kappa_values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
        ax2.set_ylabel("Cohen's Kappa")
        ax2.set_title('Inter-rater Agreement by Dimension')
        ax2.set_ylim(0, 1)
        plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
        
        # Add value labels on bars
        for bar, value in zip(bars, kappa_values):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{value:.3f}', ha='center', va='bottom')
        
        # 3. Distribution comparison
        ax3 = axes[1, 0]
        all_llm_scores = []
        all_human_scores = []
        
        for dim in self.dimensions:
            for conv_num in range(1, 31):
                llm_col = f'llm_{dim}_{conv_num}'
                human_col = f'human_{dim}_{conv_num}'
                
                if llm_col in self.responses.columns and human_col in self.responses.columns:
                    all_llm_scores.extend(self.responses[llm_col].dropna().tolist())
                    all_human_scores.extend(self.responses[human_col].dropna().tolist())
        
        ax3.hist(all_llm_scores, bins=3, alpha=0.7, label='LLM Ratings', density=True)
        ax3.hist(all_human_scores, bins=3, alpha=0.7, label='Human Ratings', density=True)
        ax3.set_xlabel('Rating Score')
        ax3.set_ylabel('Density')
        ax3.set_title('Rating Distribution Comparison')
        ax3.legend()
        ax3.set_xticks([0, 1, 2])
        
        # 4. Agreement level breakdown
        ax4 = axes[1, 1]
        agreement_levels = []
        agreement_percentages = []
        
        for dim in self.dimensions:
            if dim in agreement_data:
                agreement_levels.extend(['Exact', 'Within-1'])
                agreement_percentages.extend([
                    agreement_data[dim]['exact_agreement'],
                    agreement_data[dim]['within_one_agreement']
                ])
        
        if agreement_percentages:
            colors = ['#ff7f0e', '#2ca02c'] * len(self.dimensions)
            bars = ax4.bar(range(len(agreement_levels)), agreement_percentages, color=colors)
            ax4.set_ylabel('Agreement Percentage')
            ax4.set_title('Agreement Levels Across Dimensions')
            ax4.set_xticks(range(len(agreement_levels)))
            ax4.set_xticklabels(agreement_levels)
            ax4.set_ylim(0, 100)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Visualizations saved to: {save_path}")
        
        return fig
    
    def generate_report(self, output_file: str = "empathy_analysis_report.txt"):
        """Generate a comprehensive text report."""
        print(f"\nGenerating comprehensive report...")
        
        correlations = self.calculate_correlations()
        agreement = self.calculate_agreement_metrics()
        consistency = self.analyze_human_consistency()
        
        with open(output_file, 'w') as f:
            f.write("EMPATHY EVALUATION STUDY: ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("STUDY OVERVIEW\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total Responses: {len(self.responses)}\n")
            f.write(f"Evaluation Dimensions: {', '.join([d.replace('_', ' ').title() for d in self.dimensions])}\n\n")
            
            f.write("CORRELATION RESULTS\n")
            f.write("-" * 20 + "\n")
            for dim, results in correlations.items():
                f.write(f"{dim.replace('_', ' ').title()}:\n")
                f.write(f"  Pearson r = {results['pearson_r']:.3f} (p = {results['pearson_p']:.3f})\n")
                f.write(f"  Spearman ρ = {results['spearman_r']:.3f} (p = {results['spearman_p']:.3f})\n")
                f.write(f"  Sample size: {results['n_pairs']}\n\n")
            
            f.write("AGREEMENT METRICS\n")
            f.write("-" * 20 + "\n")
            for dim, results in agreement.items():
                f.write(f"{dim.replace('_', ' ').title()}:\n")
                f.write(f"  Cohen's κ = {results['kappa']:.3f}\n")
                f.write(f"  Mean Absolute Error = {results['mae']:.3f}\n")
                f.write(f"  Exact Agreement = {results['exact_agreement']:.1f}%\n")
                f.write(f"  Within-1-Point Agreement = {results['within_one_agreement']:.1f}%\n\n")
            
            f.write("HUMAN RATER CONSISTENCY\n")
            f.write("-" * 20 + "\n")
            for dim, std_dev in consistency.items():
                f.write(f"{dim.replace('_', ' ').title()}: Average SD = {std_dev:.3f}\n")
            
            f.write("\n\nINTERPRETATION GUIDELINES\n")
            f.write("-" * 25 + "\n")
            f.write("Correlation Strength:\n")
            f.write("  r < 0.3: Weak correlation\n")
            f.write("  0.3 ≤ r < 0.7: Moderate correlation\n") 
            f.write("  r ≥ 0.7: Strong correlation\n\n")
            f.write("Cohen's Kappa Interpretation:\n")
            f.write("  κ < 0.2: Poor agreement\n")
            f.write("  0.2 ≤ κ < 0.4: Fair agreement\n")
            f.write("  0.4 ≤ κ < 0.6: Moderate agreement\n")
            f.write("  0.6 ≤ κ < 0.8: Substantial agreement\n")
            f.write("  κ ≥ 0.8: Almost perfect agreement\n")
        
        print(f"Report saved to: {output_file}")

def main():
    """Main function to run the complete analysis pipeline."""
    # Replace with your actual Google Forms export CSV file
    responses_file = "empathy_form_responses.csv"
    
    print("EMPATHY EVALUATION ANALYSIS PIPELINE")
    print("=" * 40)
    
    try:
        # Initialize analyzer
        analyzer = EmpathyAnalysisPipeline(responses_file)
        
        # Run analyses
        correlations = analyzer.calculate_correlations()
        agreement = analyzer.calculate_agreement_metrics()
        consistency = analyzer.analyze_human_consistency()
        
        # Create visualizations
        analyzer.create_visualizations()
        
        # Generate report
        analyzer.generate_report()
        
        print("\n" + "=" * 50)
        print("ANALYSIS COMPLETE!")
        print("=" * 50)
        print("Files generated:")
        print("- empathy_analysis_charts.png")
        print("- empathy_analysis_report.txt")
        
    except FileNotFoundError:
        print(f"\nError: Could not find responses file '{responses_file}'")
        print("Please export your Google Forms responses as CSV and update the filename.")
        
    except Exception as e:
        print(f"\nError during analysis: {str(e)}")
        print("Please check your data format and try again.")

if __name__ == "__main__":
    main() 