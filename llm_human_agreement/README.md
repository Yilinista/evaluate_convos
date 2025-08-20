# LLM-Human Agreement Analysis

Analysis of agreement between LLM and human evaluators on empathy ratings, with majority voting to resolve human rater disagreements.

## 📁 Structure

```
llm_human_agreement/
├── data/                              # Human evaluation CSVs (Set 1: 28, Set 2: 27 conversations)
└── analysis/
    ├── original_set1_only/            # 🟡 Initial analysis (Set 1, no majority voting)
    ├── full_dataset_majority/         # 🟢 Final analysis (55 conversations + majority voting)
    └── comparative_analysis/          # 📊 Comparisons and improvement visualizations
```

## 📈 Key Results

| Analysis | Data | Method | Spearman ρ (Dim Avg) | Spearman ρ (Overall) |
|----------|------|--------|---------------------|---------------------|
| 🟡 **Original** | Set 1 (28) | Individual | **0.325** | ~0.160 |
| 🔵 **Baseline** | Full (55) | Individual | **0.174** | **0.108** |
| 🟢 **Final** | Full (55) | Majority Voting | **0.332** | **0.171** |

**Impact of Majority Voting:**
- Dimension Average: 0.174 → 0.332 (+91% improvement)
- Overall Correlation: 0.108 → 0.171 (+58% improvement)
- Recovers to original report level (0.325 → 0.332)

## 🎯 Final Results for Research

After applying majority voting across 55 conversations:
- **Dimension-wise Spearman ρ: 0.332** (improved from 0.174, +91%)
- **Overall Spearman ρ: 0.171** (p < 0.071, improved from 0.108, +58%)
- **Absolute agreement: 42.9%**
- **Within-one agreement: 100.0%**

## 🔧 Usage

```bash
# Final analysis (recommended)
cd analysis/full_dataset_majority/
python llm_human_agreement_with_majority_voting.py

# Comparative analysis
cd analysis/comparative_analysis/
python comprehensive_analysis.py
```

**Key Scripts:**
- `full_dataset_majority/llm_human_agreement_with_majority_voting.py` - Main analysis with majority voting
- `comparative_analysis/comprehensive_analysis.py` - Compares both correlation calculation methods
- `comparative_analysis/analyze_sets_separately.py` - Set 1 vs Set 2 comparison