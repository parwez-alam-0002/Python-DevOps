#Note: if both the parent class have same method then which is (class) is mentioned first like : here Job class is mentioned first

class Person:
    def __init__(self, name):
        self.name = name
    def getMessage(self):
        print(f'This is Person class')
class Job(Person):
    def __init__(self, salary):
        self.salary = salary
        
    def getMessage(self):
        print(f'This is Job class')

class Employee(Job, Person):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)
        super().getMessage()

emp = Employee("Jennifer", 50000)
emp.details()
