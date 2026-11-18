from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from langchain_learning.common.config import LLM_PROVIDER, LLM_MODEL


def get_llm(provider=None, model=None):
    """Initialize a provider-independent chat model."""
    
    provider = provider or LLM_PROVIDER
    model = model or LLM_MODEL
    return init_chat_model(model=model, model_provider=provider)

def get_agent(
    provider=None, 
    model=None, 
    tools=[], 
    system_prompt=""
):
    """Create a configurable LangChain agent."""
    
    provider = provider or LLM_PROVIDER
    model = model or LLM_MODEL
    chat_model = get_llm(provider, model)
    
    return create_agent(
        model=chat_model,
        tools=tools,
        system_prompt=system_prompt
    )
    