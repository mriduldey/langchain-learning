from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

# This is not merely the original Python function anymore.
# The decorator creates a LangChain tool object with metadata such as its name, description, and argument schema.
# Inspect it:
print(multiply)
print("--------------------------------------")
print("name -> ", multiply.name) # multiply
print("description -> ", multiply.description) # Multiply two integers
print("args ->", multiply.args) # args -> {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}

# Note: good description matters. The model can more reliably select the appropriate tool if description is good