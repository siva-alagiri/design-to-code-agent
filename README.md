# 🤖 Design to Code Agent

An AI-powered agent that converts UI design images into 
production-ready HTML/CSS code.

## What it does
- Upload any UI design screenshot or image
- AI analyzes the design using Groq Vision (LLaMA 4)
- Generates clean HTML/CSS code automatically
- Shows live preview of generated code
- Download the HTML file instantly

## Tech Stack
- Python
- Streamlit
- LangChain
- Groq API (LLaMA 4 Scout Vision + LLaMA 3.3 70B)

## How to Run
1. Clone the repo
2. Create `.env` file with your `GROQ_API_KEY`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `streamlit run app/main.py`