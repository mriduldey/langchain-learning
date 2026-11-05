
from langchain_learning.common.main import get_llm

model = get_llm()

# In ordinery python below works
def explain_topic(topic, level):
    prompt = f"""
    Explain {topic} to a {level} developer.
    Include a code example.
    """

    return model.stream(prompt)

for level in ["junior", "senior"]:
    print(f"\n--- {level.upper()} ---\n")
    for chunk in explain_topic("langchain", level):
        print(chunk.text, end="", flush=True)
    print("\n\n")

# So why use LangChain?

# Because real applications need more than string interpolation.

# A reusable prompt should support:
# - Separating system instructions from user inputs.
# - Automatically identifying required variables.
# - Supplying predefined configuration values.
# - Inserting conversation history.
# - Integrating with other components through a common execution interface.
# That is what LangChain's prompt templates provide.