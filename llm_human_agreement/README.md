# LLM-Human Agreement Analysis

Analysis of agreement between LLM and human evaluators on empathy ratings, using majority voting to resolve disagreements between human raters.

## Overview

We analyzed empathy ratings across four dimensions (emotional reactions, explorations, interpretations, overall empathy) on a 0-2 scale. Human evaluators rated 55 conversations total: 28 from Set 1 and 27 from Set 2.

**Two correlation methods:**
1. **Dimension average**: Calculate Spearman correlation for each dimension separately, then average
2. **Overall correlation**: Pool all scores and calculate single correlation

## Structure

```
data/
├── Empathy Evaluation - Set 1.csv    # Human ratings for 28 conversations
└── Empathy Evaluation - Set 2.csv    # Human ratings for 27 conversations

analysis/
├── original_set1_only/               # Initial analysis (Set 1 only, no majority voting)
├── full_dataset_majority/            # Main analysis (all 55 conversations + majority voting)
└── comparative_analysis/             # Comparisons and additional visualizations
```

## Results

| Analysis | Data | Method | Spearman ρ (Dim Avg) | Spearman ρ (Overall) | Absolute Agreement |
|----------|------|--------|---------------------|---------------------|-------------------|
| Original | 28 conversations | Individual ratings | **0.325** | 0.160 | 42.0% |
| Baseline | 55 conversations | Individual ratings | **0.174** | 0.108 | 42.4% |
| **Final** | 55 conversations | **Majority voting** | **0.332** | **0.171** | **42.9%** |

**Key finding:** Majority voting improved correlation from 0.174 to 0.332 (+91%), recovering to the original study level.

## Majority Voting Details

When human raters disagreed, we used the most common rating as the final score. Across all ratings:
- 18.7% had unanimous agreement
- 76.8% required majority voting
- 4.5% had ties (resolved by standard procedures)

## Usage

**Main analysis:**
```bash
cd analysis/full_dataset_majority/
python llm_human_agreement_with_majority_voting.py
```

**Key files:**
- `full_dataset_majority/llm_human_agreement_with_majority_voting.py` - Main analysis with majority voting
- `comparative_analysis/comprehensive_analysis.py` - Compares both correlation methods
- `comparative_analysis/analyze_sets_separately.py` - Set 1 vs Set 2 comparison