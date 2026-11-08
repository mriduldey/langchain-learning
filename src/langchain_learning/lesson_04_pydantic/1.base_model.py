from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str
    age: int
    email: str
    height: float | None = None # Optional field with default value of None
    

person1 = Person(name="Alice", age=30, email="alice@example.com")
print(person1)
print(person1.name)
print(person1.age)
print(person1.email)

class Employee(BaseModel):
    employee_id: str
    name: str
    age: int = Field(ge = 18, le = 80, description="The age of the employee")  # Required field with description
    department: str = Field(..., description="The department the employee belongs to")  # Required field with description
    email: str = Field(..., description="The email address of the employee")  # Required field with description
    
employee1 = Employee(name="Bob", age=25, email="bob@example.com", employee_id="E001", department="Engineering")
print(employee1)
print(employee1.name)
print(employee1.age)
print(employee1.email)
print(employee1.employee_id)
print(employee1.department)