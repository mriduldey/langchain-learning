from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

result = multiply.invoke({
    "a": 10,
    "b": 100
})

print(result) # 1000