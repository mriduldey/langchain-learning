from pydantic import BaseModel, model_validator

class ReviewIssue(BaseModel):
    title: str
    description: str
    
    @model_validator(mode="before")
    @classmethod
    def validate_title_and_description(cls, values):
        title = values.get("title", "").strip()
        description = values.get("description", "").strip()
        
        if len(title) < 5:
            raise ValueError("Title must be at least 5 characters long.")
        
        if len(description) < 10:
            raise ValueError("Description must be at least 10 characters long.")
        
        # The validator can both verify and transform the fields.
        # Here it removes leading and trailing whitespace, then returns the normalized values.
        values["title"] = title + " xyz"
        values["description"] = description
        
        return values

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