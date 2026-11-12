# model_dump_json converts a model to a JSON string

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    
# Example usage of model_dump_json
person = Person(name="Alice", age=30)

print(person.model_dump_json())  # Output: '{"name": "Alice", "age": 30}'