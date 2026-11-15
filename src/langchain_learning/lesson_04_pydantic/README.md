# Lesson 4: Pydantic

## What this folder contains

The top-level Python files in this folder are five examples of Pydantic models and validation. They progress from defining model fields to validating constrained values and nested models. The custom-validator and essential-method examples are documented in their own subfolders.

## 1. Base model — `1.base_model.py`

`Person` and `Employee` are Pydantic models, so creating an instance validates the supplied values against the declared fields.

- `Person` requires `name`, `age`, and `email`. Its `height` field is optional and defaults to `None`.
- `Employee` requires an employee ID, name, age, department, and email. `Field` restricts age to 18–80 and adds descriptions to fields.

### Example

```python
person1 = Person(name="Alice", age=30, email="alice@example.com")
```

Because `height` was omitted, this instance uses `height=None`. The script prints the model and then accesses its fields, such as `person1.name`.

The employee example supplies all required fields:

```python
employee1 = Employee(
    name="Bob",
    age=25,
    email="bob@example.com",
    employee_id="E001",
    department="Engineering",
)
```

The age value `25` is within the declared range. A value outside 18–80 fails that field's constraint.

## 2. Type coercion — `2.type_coercion.py`

This example compares Pydantic's default type coercion with strict validation.

### Example and flow

```python
student = Student(name="Charlie", age="20")
print(student)
```

The age is provided as a string, and the example demonstrates Pydantic converting it to the integer `20`.

The script next tries a string age with strict validation enabled:

```python
strict_student = StrictStudent(name="David", age="20")
```

That construction raises a validation error because `age` is declared as an integer and strict mode is enabled. The error is not caught, so normal execution stops there; the later field-level strict example is not reached in that run.

## 3. Literal values — `3.literals.py`

`Literal` restricts `ReviewIssue.issue_type` to exactly `"bug"`, `"feature"`, or `"documentation"`.

### Example and flow

```python
review_issue = ReviewIssue(
    issue_type="bug",
    description="There is a critical bug in the application.",
)
print(review_issue)
```

The `"bug"` value is one of the allowed values, so the model is printed. The script then tries `"invalid_type"`; that validation error is caught, and it prints `Literal validation error` rather than the error details.

## 4. Enums — `4.enums.py`

The `Severity` enum defines `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`. `ReviewIssue.severity` uses that enum as its field type.

### Example and flow

```python
issue = ReviewIssue(title="SQL injection", severity=Severity.HIGH)
print(issue.severity)        # Severity.HIGH
print(issue.severity.value)  # high
```

The example shows the enum member and its underlying string value. It then tries `"extreme"`, which is not a declared enum value; the validation error is caught and the script prints `Enum validation error`.

## 5. Nested Pydantic model — `5.nested-pydantic-model.py`

`Issue` describes one issue. `ReviewIssue.issue` is a list of `Issue` models, and each issue's severity is limited to `"low"`, `"medium"`, `"high"`, or `"critical"`.

### Example and flow

```python
review_issue = ReviewIssue(
    summary="Code review for the new feature",
    issue=[
        Issue(title="SQL injection vulnerability", severity="high"),
        Issue(title="Missing input validation", severity="medium"),
    ],
)
print(review_issue.issue[0])
```

Pydantic validates the nested `Issue` values while creating `ReviewIssue`. The final line prints the first issue, titled `"SQL injection vulnerability"`.
