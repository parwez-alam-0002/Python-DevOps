#Encapsulation:
'''
Hiding all the details and exposing only what neccesary details.
'''
class Bank:
    def __init__(self,balance,eid):
        self.balance=balance
        self.eid=eid
    
    #declaring protected method
    def _show_balance(self):
        print(f'Account balance is {self.balance}.')
        
    #declaring private method
    def __depositeBalance(self,amount):
        self.balance+=amount
       
    #public method 
    def checkDetails(self,eid,amt):
        if self.eid==eid and amt>-1:
            self.__depositeBalance(amt)
            self._show_balance()
        else:
            print(f'Enter the correct details')
            
person=Bank(10000,101)
person.checkDetails(101,1000)

        
        
