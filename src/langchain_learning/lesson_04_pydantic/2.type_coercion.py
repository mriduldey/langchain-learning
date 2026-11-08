from pydantic import BaseModel, ConfigDict, Field

# Default behavior of Pydantic is to coerce types when possible. 
# For example, if you define a field as an int, but provide a string that can 
# be converted to an int, Pydantic will automatically perform the conversion.
class Student(BaseModel):
    name: str
    age: int

student = Student(name="Charlie", age="20") # age will coerced from str to int -> o/p name='Charlie' age=20

print(student)


# Configure Pydantic to enforce strict type checking by setting the `strict` parameter to `True` in the model configuration.
class StrictStudent(BaseModel):
    model_config = ConfigDict(strict=True)  # This will enforce strict type checking for all fields in the model
    name: str
    age: int
    
strict_student = StrictStudent(name="David", age="20")  # This will raise a validation error because age is provided as a string

# Strict mode can be enabled by using the `strict` parameter in the field definition.
class StrictFieldStudent(BaseModel):
    name: str
    age: int = Field(..., strict=True)  # This will enforce strict type checking for the age field only

# This will raise a validation error because age is provided as a string
strict_field_student = StrictFieldStudent(name="Eve", age="20")  