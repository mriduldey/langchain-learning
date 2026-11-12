from langchain_learning.common.main import get_llm

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

class Person(BaseModel):
    name: str = Field(..., description="The person's name")
    age: int = Field(..., description="The person's age")
    email: str = Field(..., description="The person's email address")
    
structured_model = get_llm().with_structured_output(
    Person,
    method="json_schema",
    strict=True
)

# Create a reusable prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Extract person details from the text. "
        "Do not invent missing information."
    ),
    (
        "human",
        "{text}"
    )
])

# Compose using LCEL
chain = prompt | structured_model

result = chain.invoke({
    "text": "Ira is 2 months old and lives in Bangalore."
})

print(result)
print(type(result))