#Functions within Functions

def outerFunction():
    name='Shaikh Parwez Alam'
    age=25

    def innerFunction():
        print(f'Hi, I am {name}')
        print(f'My age is {age}')

    innerFunction()

outerFunction()
