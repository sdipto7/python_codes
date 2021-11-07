class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def display_details(self):
        print(f"Name:{self.name}, ID:{self.id}, age: {self.age}")

student = Student('Dipto', '20141036', '23')
# print(student.__doc__)
print(student.__dict__)
# print(student.__module__)