from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain.tools import tool

from langchain_learning.common.main import get_llm

# Define tools --------------------------------------------------------------------------
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the product"""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the sum"""
    return a + b

tools = [multiply, add]
tools_by_name = {tool.name: tool for tool in tools}

model = get_llm().bind_tools(tools)

messages: list[BaseMessage] = [
    HumanMessage(
        content = "Multiply 12 by 8, then add 10."
    )
]

MAX_STEPS = 6

for _ in range(MAX_STEPS):
    print("---------------------------------------")
    print("Step ", _, " start")
    
    print("Thinking...")
    
    response = model.invoke(messages)
    
    messages.append(response)
    # print(response)
    if not response.tool_calls:
        print("Final result: ", response.content[0]["text"])
        break
    
    for tool_call in response.tool_calls:
        # print(tool_call)
        print("Using tool -> ", tool_call["name"])
        
        result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        
        messages.append(
            ToolMessage(content=str(result), tool_call_id=tool_call["id"])
        )
        
    print("Step ", _, " end")
    print("---------------------------------------")


