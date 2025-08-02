import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.credentials import Credentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("IBM_API_KEY")
REGION = os.getenv("REGION")
MODEL_ID = os.getenv("MODEL_ID")
PROJECT_ID = os.getenv("PROJECT_ID")  # used only when creating ModelInference, not credentials

# Create credentials (NO project_id here)
creds = Credentials(
    api_key=API_KEY,
    url=f"https://{REGION}.ml.cloud.ibm.com"
)

# Initialize model inference
model = ModelInference(
    model_id=MODEL_ID,
    credentials=creds,
    project_id=PROJECT_ID
)

# Ask for idea
idea = input("Enter your startup idea: ")

# Sections to query
sections = [
    "Market Opportunity",
    "Business Model",
    "Estimated Budget",
    "Go-to-Market Strategy",
    "Potential Competitors",
    "Revenue Streams",
    "Risks and Challenges",
    "Key Performance Indicators (KPIs)"
]

# Clear old output
with open("output.txt", "w") as f:
    f.write(f"📦 Startup Blueprint for: {idea}\n\n")

# Loop through each section
for section in sections:
    prompt = f"Generate the '{section}' section of a startup business plan for this idea: {idea}"
    try:
        response = model.generate_text(prompt)
        with open("output.txt", "a") as f:
            f.write(f"\n\n{section}:\n{response.strip()}")
        print(f"✅ {section} written.")
    except Exception as e:
        print(f"❌ Error in {section}: {e}")

print("\n✅ All sections saved to output.txt")