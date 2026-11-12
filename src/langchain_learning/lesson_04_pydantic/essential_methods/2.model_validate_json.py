# model_validate_json(json_str) is a Pydantic v2 method that parses a JSON string, validates its data, and 
# returns a Pydantic model instance.

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

# Example usage of model_validate_json
json_str = '{"name": "Alice", "age": 30}'
person = Person.model_validate_json(json_str)

print(person)  # Output: name='Alice' age=30