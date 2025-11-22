class Father:
    def __init__(self):
        self.__salary=100000

    def showBalance(self)->int:
        return self.__salary
    

class Son1(Father):
    def __init__(self,salary):
        super().__init__()
        self.salary=salary

    def showSalary(self):
        amt=self.showBalance()
        print(f'Son1 Property is {self.salary+amt}')

class Son2(Father):
    def __init__(self,salary):
        super().__init__()
        self.salary=salary

    def showSalary(self):
        amt=self.showBalance()
        print(f'Son2 Property is {self.salary+amt}')

s1=Son1(1000)
s1.showSalary()
s2=Son2(2000)
s2.showSalary()