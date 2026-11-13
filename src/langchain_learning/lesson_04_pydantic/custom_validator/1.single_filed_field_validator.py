from pydantic import BaseModel, field_validator

class ReviewIssue(BaseModel):
    title: str
    description: str
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()
        
        if len(value) < 5:
            raise ValueError("Title must be at least 5 characters long.")
        
        # The validator can both verify and transform the field.
        # Here it removes leading and trailing whitespace, then returns the normalized title.
        return value + "xyz"

# Correct usage
issue = ReviewIssue(
    title="  SQL injection vulnerability  ",
    description="This issue describes a potential SQL injection vulnerability in the code."
)
print(issue)
print("-----------------------------------------------------------")

# Incorrect usage (will raise a validation error)
try:
    invalid_issue = ReviewIssue(
        title="Bug",
        description="This issue describes a minor bug in the code."
    )
except ValueError as e:
    print(f"Validation error: {e}")