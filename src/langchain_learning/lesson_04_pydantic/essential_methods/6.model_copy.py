from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

# Example usage of model_copy
person1 = Person(name="Alice", age=30)

person2 = person1.model_copy()

print("person1 ==> ", person1)  # Output: name='Alice' age=30
print("person2 ==> ", person2)  # Output: name='Alice' age=30