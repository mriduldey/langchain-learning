
# Separate Generation and Validation Schemas
#
# 1. Generation Schema (LLM-facing):
#    Defines the expected LLM output structure using basic field types.
#    Avoids constraints unsupported by some providers (e.g., Claude).
#
# 2. Validation Schema (Application-facing):
#    Enforces business rules using Pydantic (e.g., min_length, ge).
#    Works independently of the LLM provider (OpenAI, Claude, Gemini).
#
# Why separate them?
# - LangChain is provider-agnostic, but providers support different JSON Schema constraints.
# - Unsupported constraints may cause API errors or require schema transformation.
# - LLMs may generate invalid data even when instructed to follow rules.
# - Pydantic ensures invalid data is rejected before application use.
# - Allows switching LLM providers without changing business validation rules.
#
# 
# Flow:
# 1. User Input         → Send the input text to the LangChain application.
# 2. Prompt             → Format the input using ChatPromptTemplate (if used).
# 3. Generation Schema  → LangChain converts the Pydantic schema into a provider-compatible JSON Schema.
# 4. LLM API            → Provider receives the prompt and schema, then generates structured data.
# 5. Output Parsing     → LangChain parses the LLM response into a GeneratedIssue object.
# 6. model_dump()       → Convert the GeneratedIssue object into a Python dictionary.
# 7. model_validate()   → Validate the dictionary against the stricter ValidatedIssue schema.
# 8. Business Rules     → Reject invalid data (e.g., title too short or line < 1).
# 9. Application        → Use the validated object in APIs, databases, or other workflows.
#
# Note: Two schemas are optional. Use one schema when provider compatibility
# and application validation requirements can both be satisfied.


from pydantic import BaseModel, Field

from langchain_learning.common.main import get_llm


# LLM provider-facing schema
class GeneratedIssue(BaseModel):
    title: str = Field(
        description="Short description of the issue"
    )
    line: int = Field(
        description="One-based source line number"
    )
    
# Application-facing validation
class ValidatedIssue(BaseModel):
    title: str = Field(min_length=5)
    line: int = Field(ge=1)

structured_model = get_llm().with_structured_output(
    GeneratedIssue,
    method="json_schema",
    strict=True,
    include_raw=True
)

generated = structured_model.invoke("Report an issue on line 12 titled ""'Missing input validation'.")

if isinstance(generated, dict):
    validated = ValidatedIssue.model_validate(
        generated["parsed"].model_dump()
    )
    print(validated)
else:
    raise TypeError(f"Expected BaseModel, got {type(generated)}")