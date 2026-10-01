# Salesforce + Claude AI Automation Demo

A portfolio-ready demonstration of an AI-assisted CRM automation workflow using Salesforce-style customer/case data and the Claude API.

## What this demonstrates
- Salesforce CRM data handling
- Automated extraction of relevant case/customer information
- Claude API integration for summarization and classification
- Structured JSON output from an LLM
- A workflow that can be extended to Salesforce Flow, Apex, or an external automation platform

## Architecture
Salesforce CRM → Automation / Python service → Claude API → Structured AI result → Reporting / CRM update

## Example use case
A customer support case is retrieved from Salesforce. The automation sends selected fields to Claude, which:
1. Summarizes the case
2. Classifies the issue category
3. Determines urgency
4. Extracts the next recommended action

The structured response can then be written back to Salesforce or used in a reporting workflow.

## Important
This repository is a demonstration project. It uses sample Salesforce-style data by default so that no real customer information or Salesforce credentials are exposed.

## Setup
1. Install Python 3.10+.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create `.env`:
```env
ANTHROPIC_API_KEY=your_claude_api_key
```
4. Run:
```bash
python app.py
```

## Optional Salesforce connection
To connect to a real Salesforce org, add appropriate Salesforce credentials and use the `simple-salesforce` package. Never commit credentials, tokens, or `.env` files to GitHub.

## Portfolio talking point
"This project demonstrates how CRM data can be combined with Claude API to automate repetitive analysis. Instead of manually reading every case, the workflow can retrieve Salesforce data, send relevant fields to Claude, receive structured classification and summarization, and pass the result to reporting or a CRM update step."

## Skills demonstrated
Salesforce | CRM | Claude API | Python | REST API concepts | Automation | Data Processing | JSON | AI-assisted Workflow
