# model_json_schema generates a JSON schema for the model

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    
# Example usage of model_json_schema
person = Person(name="Alice", age=30)

print(person.model_json_schema())  
# Output: {
#         'title': 'Person', 
#         'type': 'object'
#         'properties': {
#           'name': {'title': 'Name', 'type': 'string'}, 
#           'age': {'title': 'Age', 'type': 'integer'}
#         }, 
#         'required': ['name', 'age'], 
#     }