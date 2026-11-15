# Lesson 4: Custom Validators

## What this folder contains

This folder contains two examples showing custom Pydantic validation: a field validator for one field and a model validator that checks multiple fields.

## 1. Single-field validator — `1.single_filed_field_validator.py`

The `ReviewIssue` model has `title` and `description` fields. Its `field_validator` applies to `title` only.

### Example and flow

When a `ReviewIssue` is created, the validator strips whitespace from the title, checks that at least five characters remain, and appends `"xyz"` to the normalized title:

```python
issue = ReviewIssue(
    title="  SQL injection vulnerability  ",
    description="This issue describes a potential SQL injection vulnerability in the code.",
)
```

The title returned by the validator is `SQL injection vulnerabilityxyz`. The description is accepted as a regular string; this validator adds no custom description check.

The invalid example supplies `title="Bug"`. After stripping, it has fewer than five characters, so the validator raises `ValueError`; the example catches and prints that validation error.

## 2. Multi-field model validator — `2.multi_field_model_validator.py`

This example uses `model_validator(mode="before")` to inspect and transform the input values for both fields before normal model validation.

### Example and flow

The validator strips both values, checks the title and description lengths, then appends `" xyz"` to the title:

```python
issue = ReviewIssue(
    title="  SQL injection vulnerability  ",
    description="This issue describes a potential SQL injection vulnerability in the code.",
)
```

For this input, the title becomes `SQL injection vulnerability xyz`, and the description is returned without its surrounding whitespace. The valid example prints the resulting model.

The invalid example uses `title="Bug"`. It fails the title-length check, raises `ValueError`, and the surrounding `try`/`except` prints the validation error. The description-length check is also present, but that invalid example fails the title check first.
