# An agent is a system in which an LLM can select and use tools repeatedly to accomplish a task.
# In our previous example, we manually wrote:
# while True:
  # response = model.invoke(...)
  # execute_tools(...)
  # append_results(...)
  
# But modern LangChain already provides an implementation of this orchestration.

from langchain.tools import tool

from langchain_learning.common.main import get_agent

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integer and return their product"""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two integer and return their sum"""
    return a + b

tools = [multiply, add]

agent = get_agent(
    tools = tools, 
    system_prompt = "You are a mathematical assistant. Use the provided tools for calculations. Keep the final answer concise."
)

print("invoked")

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Multiply 12 by 8 and add 10."
        }
    ]
})

print(result["messages"][-1].content)

print(result["messages"][-1].content[0]["text"])