📌 AI Test Case Generation
🚀 AI-Powered QA Automation Framework

This project is an AI-driven QA framework that automatically:

Extracts structured requirements from a PRD

Generates functional, negative, and edge test cases

Analyzes test coverage

Detects coverage gaps

Exports production-ready CSV reports

🧠 Problem It Solves

AI startups struggle with:

Manual test case writing from PRDs

Missing edge case coverage

Inconsistent QA documentation

Lack of traceability and governance

This framework automates the QA analysis pipeline using LLMs.

⚙️ Architecture
PRD
  ↓
Requirement Extractor (LLM)
  ↓
Test Case Generator (LLM)
  ↓
Coverage Analyzer
  ↓
CSV Report Generator
🧪 Features

Deterministic AI output (temperature=0)

Structured JSON parsing

Markdown cleanup handling

Coverage percentage calculation

Gap detection (missing test types)

Exportable test case reports

Modular architecture

Environment-based secret management

📊 Example Output
Coverage Summary
Total Requirements: 7
Fully Covered: 7
Coverage %: 100%
Generated Files

output/testcases.csv

output/coverage_report.csv

🔐 Setup Instructions
1. Clone Repository
git clone <your-repo-link>
cd ai-testcase-generation-engine
2. Create Virtual Environment
python -m venv venv
3. Activate

Git Bash:

source venv/Scripts/activate

CMD:

venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Add OpenAI Key

Create .env file:

OPENAI_API_KEY=your_key_here
6. Run
python main.py
🎯 Why This Project Matters

This project demonstrates:

LLM output validation

AI deterministic control

AI QA governance design

Automated coverage analytics

Production-style modular engineering

👨‍💻 Built By

Rohit Kumar
AI QA Engineer | Automation | AI Testing
