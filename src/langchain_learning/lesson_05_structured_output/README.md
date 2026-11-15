# Lesson 5: Structured Output

## What this folder contains

This folder contains three examples using LangChain structured output: returning a structured result, including raw output alongside parsed output, and validating generated data with a separate Pydantic schema.

## 1. Structured output — `1.structured_output.py`

The example defines a `Person` schema with required `name`, `age`, and `email` fields, then configures the model returned by `get_llm()` to use structured output with the `"json_schema"` method and `strict=True`.

### Example and flow

The prompt asks for extraction without inventing missing information:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract person details from the text. Do not invent missing information."),
    ("human", "{text}"),
])
chain = prompt | structured_model
```

The chain is invoked with:

```python
result = chain.invoke({
    "text": "Ira is 2 months old and lives in Bangalore."
})
print(result)
print(type(result))
```

The text supplies a name, age phrase, and location, while the schema also requires an email. The script prints whatever the configured model returns and its type; this source does not establish a fixed result for the missing email.

## 2. Include raw output — `2.include_raw.py`

This example uses the same `Person` schema and prompt pattern, but configures structured output with `include_raw=True`.

### Example and flow

It invokes the chain with the same input text:

```python
result = chain.invoke({
    "text": "Ira is 2 months old and lives in Bangalore."
})
```

The script first prints `result`. If it is a dictionary, the code then reads and prints these entries:

```python
result["parsed"]
result["parsing_error"]
```

It also prints the type of `result["parsed"]`. The actual values depend on the model call; the example does not provide a fixed response. There is no `else` branch if `result` is not a dictionary.

## 3. Separate generation and validation schemas — `3.seperate_generation_and_validation_schema.py`

`GeneratedIssue` is the schema used for the structured model output. It has a string title and integer line number. `ValidatedIssue` is used afterward and adds a minimum title length of five and a minimum line number of one.

### Example and flow

The configured model is invoked with a request for an issue on line 12:

```python
generated = structured_model.invoke(
    "Report an issue on line 12 titled 'Missing input validation'."
)
```

If `generated` is a dictionary, the script converts its parsed model to a dictionary and validates that data against the stricter application schema:

```python
validated = ValidatedIssue.model_validate(
    generated["parsed"].model_dump()
)
print(validated)
```

Thus, the example's stages are: request structured output using `GeneratedIssue`, convert the parsed result with `model_dump()`, then apply `ValidatedIssue` constraints with `model_validate()`. It does not show a fixed model response or a validation failure. If `generated` is not a dictionary, the source raises a `TypeError`.
