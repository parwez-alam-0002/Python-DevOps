class Main:
    def __init__(self,name):
        self.name=name
        
    def getName(self):
        print(f'Name : {self.name}')
        
class Child(Main):
    def __init__(self,name,age):
        super().__init__(name)
        self.__age=age
        
    def getInfo(self):
        self.getName()
        print(f'Age : {self.__age}')
        
p1=Child('Sahil',25)
p1.getInfo()
        
