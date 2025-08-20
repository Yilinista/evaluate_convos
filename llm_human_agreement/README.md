# Supplementary Materials: LLM-Human Agreement Analysis

This document provides implementation details and results for the analysis of agreement between LLM-generated and human-provided empathy evaluations, with a focus on majority voting approaches to resolve inter-rater disagreements.

## Data and Methods

The analysis examines empathy ratings across four dimensions (emotional reactions, explorations, interpretations, overall empathy) using a 0-2 scale. Human evaluators (n=10) rated conversations from two sets: Set 1 (28 conversations) and Set 2 (27 conversations), totaling 55 conversations.

Two correlation calculation methods were employed:
1. Dimension-wise averaging: Spearman correlations calculated separately for each empathy dimension, then averaged
2. Overall correlation: All dimension scores pooled before correlation calculation

## Directory Structure

```
data/
├── Empathy Evaluation - Set 1.csv    (Human ratings, 28 conversations)
└── Empathy Evaluation - Set 2.csv    (Human ratings, 27 conversations)

analysis/
├── original_set1_only/               (Initial analysis: Set 1, individual ratings)
├── full_dataset_majority/            (Primary analysis: combined data, majority voting)
└── comparative_analysis/             (Supplementary comparisons and visualizations)
```

## Results

### Agreement Metrics

| Condition | N | Method | ρ_dim | ρ_overall | Absolute Agreement | Within-1 Agreement |
|-----------|---|--------|-------|-----------|-------------------|-------------------|
| Original | 28 | Individual | 0.325 | 0.160 | 42.0% | 98.9% |
| Baseline | 55 | Individual | 0.174 | 0.108 | 42.4% | 98.7% |
| Final | 55 | Majority | 0.332 | 0.171 | 42.9% | 100.0% |

Where ρ_dim represents dimension-wise averaged Spearman correlation and ρ_overall represents overall pooled correlation.

### Majority Voting Impact

Application of majority voting to resolve inter-rater disagreements resulted in substantial improvements in correlation measures. The dimension-wise correlation increased from ρ = 0.174 to ρ = 0.332 (Δρ = +0.158, 91% relative improvement). Overall correlation similarly improved from ρ = 0.108 to ρ = 0.171 (Δρ = +0.063, 58% relative improvement).

Human rater agreement patterns showed 18.7% unanimous agreement, 76.8% majority consensus, and 4.5% tied votes across all dimension-conversation pairs, indicating moderate inter-rater reliability that benefits from consensus resolution.

## Implementation

Primary analysis script: `analysis/full_dataset_majority/llm_human_agreement_with_majority_voting.py`

The majority voting implementation collects all human evaluator responses for each conversation-dimension pair and selects the most frequent rating as the consensus score. Ties are resolved according to standard voting procedures.

Comparative analyses examining Set 1 vs Set 2 differences and correlation calculation methods are available in `analysis/comparative_analysis/`.