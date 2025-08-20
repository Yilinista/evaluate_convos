# LLM-Human Agreement Analysis

Analysis of agreement between LLM and human evaluators on empathy ratings, using majority voting to resolve disagreements between human raters.

## Overview

We analyzed empathy ratings across four dimensions (emotional reactions, explorations, interpretations, overall empathy) on a 0-2 scale. Human evaluators rated 55 conversations total: 28 from Set 1 and 27 from Set 2.

**Method:** We use dimension-average Spearman correlation (calculate correlation for each dimension separately, then average) to match the original study approach.

## Structure

```
data/
├── Empathy Evaluation - Set 1.csv    # Human ratings for 28 conversations
└── Empathy Evaluation - Set 2.csv    # Human ratings for 27 conversations

analysis/
├── full_dataset_majority/            # Main analysis (all 55 conversations + majority voting)
└── comparative_analysis/             # Set comparisons with annotated visualizations

archive/                              # Less important files (original analysis, old figures)
├── original_set1_only/               # Initial Set 1 only analysis
└── [other archived files]            # Previous versions and intermediate results
```

## Results

Comparing the original study results with our majority voting approach:

| Analysis | Data | Method | Spearman ρ | Absolute Agreement | Within-1 Agreement |
|----------|------|--------|-----------|-------------------|-------------------|
| **Original Study** | ~28 conversations | Individual ratings | **0.325** | 42% | 98.9% |
| **Current (Majority Voting)** | 55 conversations | **Majority voting** | **0.332** | **42.9%** | **100.0%** |

**Key finding:** Majority voting with the complete dataset maintains and slightly improves upon the original study performance.

## Majority Voting Details

When human raters disagreed, we used the most common rating as the final score. Across all ratings:
- 18.7% had unanimous agreement
- 76.8% required majority voting
- 4.5% had ties (resolved by standard procedures)

## Usage

**Recommended analysis (clean results):**
```bash
cd analysis/full_dataset_majority/
python simplified_analysis.py
```

**Key files:**
- `simplified_analysis.py` - Clean analysis with clear results and visualization
- `annotated_majority_voting_analysis.png` - **Main comprehensive figure with descriptions**
- `llm_human_agreement_with_majority_voting.py` - Complete implementation details

**Annotated visualizations (recommended):**
- `annotated_majority_voting_analysis.png` - 9-panel comprehensive analysis with subplot descriptions
- `comparative_analysis/annotated_set_comparison_analysis.png` - Set 1 vs Set 2 comparison with explanations
- `comparative_analysis/annotated_majority_voting_improvements.png` - Impact analysis with detailed annotations

**Additional files:**
- `simplified_majority_voting_results.png` - Simple before/after comparison
- `archive/` - Previous versions and less important intermediate files