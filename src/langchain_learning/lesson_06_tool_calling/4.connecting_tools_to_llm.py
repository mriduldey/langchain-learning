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

# Note: We will not see the tool call printing (line 8 and 14). Because tool call does not invoke the tools.
# So first we send the query to LLM to get which tool need to be called and then we call the tool in our app.
# and second, we send the tool result to LLM again.
# simply there is atleast two LLM calls involved here during tool call.
 
# Note: For complex scenarios(for Agents) there will be multiple tool call, LLM will observe the result from tools and 
# may tool call again untill the goal is reached 