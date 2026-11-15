from langchain.tools import tool

from langchain_learning.common.main import get_llm

@tool
def multiply(a: int, b: int) -> int:
    "Multiply two integers and reqturn their product."
    print("multiply tool is called.")
    return a * b

@tool
def add(a: int, b: int) -> int:
    "Add two integers and return the sum."
    print("Addition tool is called.")
    return a + b

model = get_llm()

response_normal = model.invoke(
    "Multiply 50 with 1000."
)

model_with_tools = model.bind_tools([multiply, add])

response_multi = model_with_tools.invoke(
    "What is 125 multiplied by 48?"
)

response_add = model_with_tools.invoke(
    "What is 125 added with 48?"
)

# check content has response, but tool calls is empty[]
print("Without tool call -> ", response_normal) 

print("=======================================================")

# Check content is empty [], but tool calls is not empty and tool returned is 'add'
print("Add -> ", response_add) 
print("=======================================================")

# Check content has empty response [], but tool calls is not empty and tool returned is 'multiply'
print("Multiply -> ", response_multi)