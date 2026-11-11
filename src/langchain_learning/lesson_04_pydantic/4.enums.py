from enum import Enum
from pydantic import BaseModel

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