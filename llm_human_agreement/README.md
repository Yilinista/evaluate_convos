# LLM-Human Agreement Analysis

Analyzes agreement between LLM and human evaluators in assessing chatbot empathy.

## Data
- **Input**: 28 conversations × 5 human evaluators × 4 empathy dimensions
- **Source**: Google Forms (Prolific study) + LLM evaluations (Gemini/GPT-4)
- **Scale**: 0-2 (Not at all / Somewhat / Strongly present)

## Metrics

| Metric | Result | Interpretation |
|--------|--------|----------------|
| **Absolute Agreement** | 42.0% | LLM and human give exact same score |
| **Spearman Correlation** | ρ=0.325 (p<0.001) | Weak positive correlation |
| **Within-One Agreement** | 98.9% | Scores differ by ≤1 point |
| **Krippendorff's Alpha** | α=0.429 | Low inter-rater reliability among humans |

## Per-Dimension Results

| Dimension | Agreement | Spearman ρ | Krippendorff α |
|-----------|-----------|------------|----------------|
| Emotional Reactions | 33.6% | 0.342 | 0.420 |
| Explorations | 55.7% | 0.308 | 0.412 |
| Interpretations | 35.7% | 0.355 | 0.415 |
| Overall Empathy | 42.9% | 0.296 | 0.467 |

## Usage

```bash
pip install pandas numpy scipy matplotlib seaborn krippendorff
python llm_human_agreement_analysis.py
```

## Output
- `llm_human_agreement_analysis.png` - Visualization dashboard
- `llm_human_agreement_summary.csv` - Statistical summary

## Key Finding
LLM-human agreement (42%) is reasonable given low human inter-rater reliability (α=0.429), suggesting empathy assessment is inherently subjective.