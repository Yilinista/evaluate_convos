# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a research project for empathy evaluation in chatbot conversations. It generates Google Forms for Prolific studies comparing human and LLM empathy evaluations using conversation data from WhatsApp chatbot interactions.

## Architecture

The project consists of three main components:

1. **Data Processing Pipeline** (`create_forms.py`)
   - Loads conversation data from `evaluated_bot_chats/` directory structure
   - Processes JSON files containing chatbot conversation logs with empathy scores
   - Generates Google Apps Script code for form creation

2. **Google Apps Script Generator** (`empathy_evaluation_form.gs`)
   - Generated script that creates Google Forms with conversation displays
   - Implements 4-dimension empathy rating grids (Emotional Reactions, Explorations, Interpretations, Overall Empathy)
   - Designed for Prolific participant studies

3. **Analysis Pipeline** (`analysis_pipeline.py`)
   - Post-collection analysis of Google Forms responses
   - Calculates correlations, agreement metrics, and human rater consistency
   - Generates visualizations and statistical reports

## Data Structure

Expected data format in `evaluated_bot_chats/`:
```
evaluated_bot_chats/
├── round_1/message_logs.json
├── round_2/message_logs.json  
└── round_3/message_logs.json
```

Each JSON contains participant conversations with LLM-generated empathy scores on a 0-2 scale.

## Common Commands

### Generate Google Forms Script
```bash
python create_forms.py
```
This creates `empathy_evaluation_form.gs` ready for Google Apps Script deployment.

### Run Analysis Pipeline
```bash
# Install dependencies first
pip install pandas numpy scipy scikit-learn matplotlib seaborn

# Run analysis
python analysis_pipeline.py
```
Requires `empathy_form_responses.csv` exported from Google Forms.

### Configuration Options
- Modify conversation count: Adjust `max_conversations` parameter in `create_forms.py:407`
- Text truncation: Modify truncation length in generated script template
- Analysis parameters: Configure dimension mappings in `analysis_pipeline.py:38-42`

## Key Implementation Details

- **Form Generation**: Uses Google Apps Script FormApp API to create multi-page forms
- **Empathy Scoring**: 4 dimensions rated on 0-2 scale (Not at all / Somewhat / Strongly present)
- **Data Analysis**: Calculates Pearson/Spearman correlations, Cohen's Kappa, and agreement percentages
- **Conversation Processing**: Handles WhatsApp format messages, filters by empathy score availability

## Output Files

- `empathy_evaluation_form.gs` - Google Apps Script for form creation
- `empathy_analysis_charts.png` - Visualization output from analysis
- `empathy_analysis_report.txt` - Statistical summary report