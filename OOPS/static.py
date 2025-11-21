class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        
dg=Dog(age=2,name='Tommy')
print(f'name = {dg.name} age = {dg.age} species = {dg.species}')
tom=Dog(name='lucky',age=10)
print(f'name = {tom.name} age = {tom.age} species = {tom.species}')
