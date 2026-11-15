from langchain.tools import tool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(
        description = "First integer"
    )
    b: int = Field(
        description = " Second integer"
    )

@tool(args_schema = MultiplyInput)
def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

if isinstance
print(multiply.args_schema.model_json_schema())

result = multiply.invoke({
    "a": 10,
    "b": 100
})

print("-----------------------------------------------")
print(result) # 1000


# For simple tools such as:
# @tooldef square(n: int) -> int:    
#     """Return the square of a number."""    
#     return n * n

# the automatically inferred schema is sufficient.

# For more complex tools such as:
# search_issues(repository="my-repo",    
#               state="open",    
#               labels=["bug", "urgent"],    
#               limit=20
# )

# an explicit Pydantic schema makes the contract easier to maintain and review.