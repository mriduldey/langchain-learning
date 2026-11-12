# model_dump converts a model to a Python dictionary

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    
# Example usage of model_dump
person = Person(name="Alice", age=30)

print(person.model_dump())  # Output: {'name': 'Alice', 'age': 30}