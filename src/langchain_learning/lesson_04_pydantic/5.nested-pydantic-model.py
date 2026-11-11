from pydantic import BaseModel
from typing import Literal

class Issue(BaseModel):
    title: str
    severity: Literal["low", "medium", "high", "critical"]

class ReviewIssue(BaseModel):
    summary: str
    issue: list[Issue]

# Pydantic validates nested models automatically.
# This is a foundational capability for transforming generated LLM output into 
# reliable application data structures.
# --------------------
# Example usage
review_issue = ReviewIssue(
    summary="Code review for the new feature",
    issue=[
        Issue(title="SQL injection vulnerability", severity="high"),
        Issue(title="Missing input validation", severity="medium"),
    ]
)

print(review_issue.issue[0])

