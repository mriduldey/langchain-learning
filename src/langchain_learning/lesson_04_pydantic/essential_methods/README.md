# Lesson 4: Essential Pydantic Methods

## What this folder contains

This folder contains six small examples of Pydantic model methods for validating input, serializing a model, generating its JSON Schema, and copying a model. Each example defines a `Person` model with `name` and `age` fields.

## 1. Validate Python data — `1.model_validate.py`

`model_validate()` takes Python data and validates it against the model.

### Example and flow

```python
data = {"name": "Alice", "age": 30}
person = Person.model_validate(data)
print(person)
```

The dictionary satisfies the model fields, so the method returns a `Person` instance (`name='Alice' age=30`). The script then tries `{"name": "Bob", "age": "thirty"}`. That value cannot be validated as an integer age; the example catches and prints the validation error.

## 2. Validate JSON — `2.model_validate_json.py`

`model_validate_json()` accepts a JSON string, parses it, and validates the resulting data against the model.

### Example and flow

```python
json_str = '{"name": "Alice", "age": 30}'
person = Person.model_validate_json(json_str)
print(person)
```

The JSON contains both required fields, so the script prints the resulting `Person` instance.

## 3. Serialize to a Python dictionary — `3.model_dump.py`

`model_dump()` converts a model instance into a Python dictionary.

### Example and flow

```python
person = Person(name="Alice", age=30)
print(person.model_dump())
```

The example's printed result is `{'name': 'Alice', 'age': 30}`.

## 4. Serialize to JSON — `4.model_dump_json.py`

`model_dump_json()` converts a model instance into a JSON string.

### Example and flow

```python
person = Person(name="Alice", age=30)
print(person.model_dump_json())
```

The source comment gives the JSON representation as `{"name": "Alice", "age": 30}`; the method returns it as a JSON string.

## 5. Generate JSON Schema — `5.model_json_schema.py`

`model_json_schema()` generates a schema describing the `Person` model's fields.

### Example and flow

```python
print(person.model_json_schema())
```

The printed dictionary describes an object with `name` as a string and `age` as an integer, and lists both fields as required. The source creates a `Person` instance before this call, but the schema describes the model rather than using that instance's values.

## 6. Copy a model — `6.model_copy.py`

`model_copy()` creates another model from an existing instance.

### Example and flow

```python
person1 = Person(name="Alice", age=30)
person2 = person1.model_copy()

print("person1 ==> ", person1)
print("person2 ==> ", person2)
```

The script prints both model values; in this example, each displays `name='Alice' age=30`.
