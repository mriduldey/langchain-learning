from langchain.chat_models import init_chat_model
from langchain_learning.config import LLM_PROVIDER, LLM_MODEL


def get_llm(provider=None, model=None):
    provider = provider or LLM_PROVIDER
    model = model or LLM_MODEL
    return init_chat_model(model=model, model_provider=provider)


model = get_llm()
prompt = f"""Write a short poem about the beauty of {LLM_PROVIDER} and {LLM_MODEL}."""

for chunk in model.stream(prompt):
    print(chunk.text, end="", flush=True)