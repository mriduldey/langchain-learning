import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google_genai")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.8-flash")