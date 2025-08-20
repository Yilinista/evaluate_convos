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
├── original_set1_only/               # Initial analysis (Set 1 only, no majority voting)
├── full_dataset_majority/            # Main analysis (all 55 conversations + majority voting)
└── comparative_analysis/             # Comparisons and additional visualizations
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
- `simplified_majority_voting_results.png` - Main visualization showing recovery to original performance
- `llm_human_agreement_with_majority_voting.py` - Complete implementation details

**Additional analyses (for detailed comparisons):**
- `comparative_analysis/` - Detailed method comparisons and validation analyses