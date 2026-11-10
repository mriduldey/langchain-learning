from typing import Literal
from pydantic import BaseModel
from enum import Enum

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

print("Enum----------------------------------------------------------------- Enum")

class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ReviewIssue(BaseModel):
    title: str
    severity: Severity

# Valid
issue = ReviewIssue(
    title = "SQL injection",
    severity = Severity.HIGH
)

print(issue.severity)        # Severity.HIGH
print(issue.severity.value)  # high

print("-----------------------------------------------------------------")

# Invalid - raises Pydantic ValidationError
try:
    invalid_issue = ReviewIssue(
        title = "Invalid severity",
        severity = "extreme"  # Not a valid Severity enum value
    )
except Exception:
    print("Enum validation error")
