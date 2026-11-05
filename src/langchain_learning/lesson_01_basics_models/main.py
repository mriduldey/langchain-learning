from langchain_learning.common.main import get_llm
from langchain_learning.config import LLM_PROVIDER, LLM_MODEL

model = get_llm()
prompt = f"""Write a short poem about the beauty of {LLM_PROVIDER} and {LLM_MODEL}."""

for chunk in model.stream(prompt):
    print(chunk.text, end="", flush=True)