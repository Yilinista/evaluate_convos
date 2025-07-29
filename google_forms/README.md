# Google Apps Script Generator for Empathy Evaluation Forms

Generates Google Forms for Prolific studies comparing human and LLM empathy evaluations.

**Requirements:** Python 3.7+ with `json` and `os` modules (included in standard library)

## Overview

Creates forms with:
- **4 empathy dimensions**: Emotional Reactions, Explorations, Interpretations, Overall Empathy
- **Human rating grids** for each conversation
- **Streamlined for Prolific** (consent handled by platform)

## Files

- `create_forms.py` - Main generator script
- `empathy_evaluation_form.gs` - Generated Google Apps Script
- `analysis_pipeline.py` - Post-collection analysis

## Data Format

```
evaluated_bot_chats/
├── round_1/message_logs.json
├── round_2/message_logs.json  
└── round_3/message_logs.json
```

Each JSON:
```json
{
  "participant_id": {
    "current_session": [{"role": "assistant", "content": "..."}, ...],
    "session_1": [{"role": "user", "content": "..."}, ...],
    "current_session_score_emotional_reactions": 1,
    "current_session_score_explorations": 2,
    "current_session_score_interpretations": 1,
    "current_session_score_empathy": 1,
    "session_1_score_emotional_reactions": 0,
    "session_1_score_explorations": 2,
    "session_1_score_interpretations": 1,
    "session_1_score_empathy": 1
  }
}
```

## Quick Start

1. **Generate**: `python create_forms.py`
2. **Deploy**: Copy `empathy_evaluation_form.gs` to [script.google.com](https://script.google.com)
3. **Run**: Execute `createEmpathyEvaluationForm()` function
4. **Grant Permissions**: Allow Google Apps Script to create forms and access Drive
5. **Use**: Share form URL with Prolific participants

## Configuration

```python
# Modify conversation count
script_code = generator.generate_apps_script(max_conversations=20)

# Adjust truncation length
const conversationText = truncateText(conversation.text, 800);
```

## Analysis

After data collection:

```python
# Install dependencies
pip install pandas numpy scipy scikit-learn matplotlib seaborn

# Run analysis
python analysis_pipeline.py
```

Outputs:
- `empathy_analysis_charts.png` - Visualizations
- `empathy_analysis_report.txt` - Statistical summary
- Correlation coefficients and agreement metrics

## Troubleshooting

- **Script fails**: Check Google Apps Script permissions and JSON format
- **Form empty**: Verify empathy scores exist and are integers
- **Slow loading**: Reduce `max_conversations` parameter
- **Permission denied**: Ensure Google account can create forms and access Drive


