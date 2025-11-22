class Bank:
    def __init__(self,name,balance):
        self.__name=name
        self.__id=id
        self.__balance=balance
    
    def getBalance(self):
        print(f'{self.__name} balance is : {self.__balance}')

    def deposite(self,amt):
        self.__balance+=amt


class Postal:
    def __init__(self, salary, name):
        self.__salary=salary
        self.__name=name

    def getBalance(self):
        print(f'{self.__name} salary is : {self.__salary}')


class Employee(Postal,Bank):
    def __init__(self,amount,name,salary):
        Bank.__init__(self,name,amount)
        Postal.__init__(self,salary,name)

    def callFn(self,amt):
        self.deposite(amt)
        Postal.getBalance(self)
        Bank.getBalance(self)


emp=Employee(2000,'Parwez Alam',40000)
emp.callFn(1000)
