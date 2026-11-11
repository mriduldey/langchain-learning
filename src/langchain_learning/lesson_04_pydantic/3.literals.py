from typing import Literal
from pydantic import BaseModel

print("Literal----------------------------------------------------------------- Literal")

class ReviewIssue(BaseModel):
    issue_type: Literal["bug", "feature", "documentation"]
    description: str

# Example usage
review_issue = ReviewIssue(issue_type="bug", description="There is a critical bug in the application.")
print(review_issue)

print("-----------------------------------------------------------------")

# Wrong example that will raise a validation error
try:
    invalid_review_issue = ReviewIssue(issue_type="invalid_type", description="This will raise a validation error.")
except Exception:
    print("Literal validation error")
