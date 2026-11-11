# 1. model_validate: This method is used to validate the input data against the model's schema. It checks if the provided data 
# conforms to the expected types and constraints defined in the model. If the data is valid, it returns an instance of 
# the model; otherwise, it raises a validation error.

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    
# Example usage of model_validate
data = {"name": "Alice", "age": 30}

person = Person.model_validate(data)
print(person)  # Output: name='Alice' age=30

print("|||||||||||||||||||||||||||||||||||||||||")

# Example of invalid data
invalid_data = {"name": "Bob", "age": "thirty"}  # age should be an int
try:    
    invalid_person = Person.model_validate(invalid_data)    
except Exception as e:
    print(f"Validation error: {e}")  # Output: Validation error: 1 validation error for Person