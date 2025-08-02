
#  Startup Blueprint Generator Agent

A simple Agentic AI project powered by **IBM Watsonx Granite** (`granite-3-3-8b-instruct`) that transforms raw startup ideas into structured, actionable business blueprints

# How It Works

1. You enter a startup idea (e.g., _"a cake delivery app for home bakers"_)
2. The IBM Granite LLM processes your idea
3. It generates a detailed business plan including:
   - Market Opportunity
   - Business Model
   - Budget Estimates
   - Go-to-Market Strategy
   - Revenue Streams, Competitors, Risks & KPIs

##  Tech Stack

- IBM Watsonx.ai
- Python (IBM Watsonx AI SDK)
- Granite LLMs (`granite-3-3-8b-instruct`)
- IBM Cloud (Lite tier used)

##  Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/dubey-git/startup-blueprint-generator---agent.git
   cd startup-blueprint-generator---agent

	2.	Add your credentials in the .env file:

IBM_API_KEY=your_api_key
REGION=us-south
PROJECT_ID=your_project_id
MODEL_ID=ibm/granite-3-3-8b-instruct


	3.	Install dependencies:

pip install -r requirements.txt


	4.	Run the app:

python app.py

# Output

Generated blueprint sections will be saved in:

output.txt

# Project Status

✅ Fully functional basic agent
✅ IBM Cloud-based deployment
✅ Generates structured startup blueprints from simple text input

📌 Notes
	•	Built as part of the IBM AI Internship Capstone Project 2025.
	•	GitHub repo link included in final PPT and PDF as required.

🧑‍💻 Author

Yash Dubey
GitHub: dubey-git
