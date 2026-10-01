import csv
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    raise RuntimeError("Set ANTHROPIC_API_KEY in your .env file.")

client = Anthropic(api_key=API_KEY)

def load_case(case_id: str):
    path = Path("data/sample_cases.csv")
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["Case_ID"] == case_id:
                return row
    return None

def analyze_case(case):
    prompt = f"""
You are an AI assistant supporting a CRM operations team.

Analyze the following Salesforce case and return ONLY valid JSON with these keys:
summary, category, priority, sentiment, next_action.

Salesforce case:
Case ID: {case['Case_ID']}
Customer: {case['Customer_Name']}
Subject: {case['Subject']}
Description: {case['Description']}
Status: {case['Status']}
"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    text = "".join(
        block.text for block in response.content
        if getattr(block, "type", None) == "text"
    )

    text = text.strip().removeprefix("```json").removesuffix("```").strip()
    return json.loads(text)

if __name__ == "__main__":
    case_id = "CASE-1001"
    case = load_case(case_id)

    if not case:
        raise RuntimeError(f"Case {case_id} not found.")

    result = analyze_case(case)

    print("\n=== Salesforce → Claude AI Automation ===")
    print(f"Case: {case_id}")
    print(json.dumps(result, indent=2))
