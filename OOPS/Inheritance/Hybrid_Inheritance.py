class Person:
    def display(self):
        print('Person class')
        
class Employee(Person):
    def display(self):
        print('Employee class')
        
class Example(Employee,Person):
    def display(self):
        Employee.display(self)
        Person.display(self)
        #print(Example.mro()) 
       
e=Example()
e.display()
