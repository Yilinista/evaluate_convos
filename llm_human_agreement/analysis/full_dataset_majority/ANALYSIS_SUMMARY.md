# Majority Voting Analysis - Core Findings

## Overview
Analysis of 55 conversations (Set 1: 28, Set 2: 27) using majority voting to resolve human rater disagreements in empathy evaluation.

## Key Results

### Performance Recovery
- **Original Study**: 0.325 Spearman correlation (~28 conversations)
- **Individual Ratings**: 0.174 correlation (55 conversations) 
- **Majority Voting**: **0.332 correlation** (55 conversations) ✅
- **Improvement**: +91% correlation recovery, matching original study performance

### Majority Voting Impact
| Metric | Individual | Majority | Improvement |
|--------|------------|----------|-------------|
| Spearman ρ (dim avg) | 0.174 | **0.332** | +91% |
| Absolute Agreement | 42.4% | **42.9%** | +0.5% |
| Within ±1 Agreement | 98.7% | **100.0%** | +1.3% |

### Human Rater Patterns
- **18.7%** - Unanimous agreement (no resolution needed)
- **76.8%** - Majority voting required to resolve disagreements  
- **4.5%** - Tied votes (resolved by standard procedures)

### Dimension-wise Performance
| Dimension | Absolute Agreement | Spearman ρ | Human Consistency |
|-----------|-------------------|------------|-------------------|
| Emotional Reactions | 32.7% | 0.248 | 73.1% |
| Explorations | **63.6%** | 0.328 | 75.3% |
| Interpretations | 30.9% | 0.378 | 71.6% |
| Overall Empathy | 56.4% | **0.451** | 74.9% |

## Core Insights
1. **Method Validation**: Majority voting successfully recovers original study performance levels
2. **Scale Effectiveness**: Works consistently across 55 conversations vs original ~28
3. **Disagreement Resolution**: ~77% of evaluations benefit from majority voting consensus
4. **Dimension Variation**: Empathy dimension shows strongest LLM-human correlation (0.451)

## Methodology
- **Calculation Method**: Dimension-average Spearman correlation (matches original study)
- **Voting Algorithm**: Most frequent rating becomes consensus score
- **Statistical Validation**: All major improvements are statistically significant (p<0.05)