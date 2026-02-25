import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_requirements(prd_text: str):
    """
    Uses LLM to extract structured requirements from PRD
    """

    prompt = f"""
    You are a Senior QA Analyst.

    Extract all testable requirements from the PRD.

    Return STRICT JSON format like this:

    [
      {{
        "requirement_id": "REQ-1",
        "description": "",
        "type": "functional"
      }}
    ]

    PRD:
    {prd_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_output = response.choices[0].message.content

    print("\nDEBUG RAW OUTPUT:\n", raw_output)

    cleaned_output = raw_output.strip()

    if cleaned_output.startswith("```"):
        cleaned_output = cleaned_output.replace("```json", "")
        cleaned_output = cleaned_output.replace("```", "")
        cleaned_output = cleaned_output.strip()

    requirements_json = json.loads(cleaned_output)

    return requirements_json