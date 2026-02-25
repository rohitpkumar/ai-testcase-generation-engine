import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_testcases(requirements: list):
    """
    Generates functional, negative and edge test cases
    for given structured requirements
    """

    prompt = f"""
    You are a Senior QA Automation Engineer.

    For each requirement below, generate:

    - At least 1 Functional test case
    - At least 1 Negative test case
    - At least 1 Edge test case

    Return STRICT JSON format like this:

    [
      {{
        "requirement_id": "REQ-1",
        "testcases": [
          {{
            "type": "functional",
            "title": "",
            "steps": ["step1", "step2"],
            "expected_result": ""
          }}
        ]
      }}
    ]

    Requirements:
    {requirements}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_output = response.choices[0].message.content

    cleaned_output = raw_output.strip()

    if cleaned_output.startswith("```"):
        cleaned_output = cleaned_output.replace("```json", "")
        cleaned_output = cleaned_output.replace("```", "")
        cleaned_output = cleaned_output.strip()

    testcases_json = json.loads(cleaned_output)

    return testcases_json