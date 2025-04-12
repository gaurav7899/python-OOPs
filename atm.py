class Atm:
    #constructor
    def __init__(self):
        self.pin=""
        self.__balance=0
        
    # getter
    def get_balance(self):
        return self.__balance
    
    #setter
    def set_balance(self,new_value):
        if type(new_value)==int:
            self.__balance=new_value
        else:
            print("chal nekal yaha se")        
        
        
        
        self.menu()
    def menu(self):
        user_input=input('''
                        1.press 1 create pin
                        2.press 2 change pin
                        3.press 3 check balance
                        4.press 4 withdraw
                        5.anything to exit
                        ''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw()
        else:
            exit()
        

    def create_pin(self):
       new_pin= input('enter the new pin:')
       self.pin=new_pin
       balance=int(input('enter the balance:'))
       self.__balance=balance
       
       self.menu()
       
    def change_pin(self):
       old_pin= input('enter the old pin:')
       self.pin=old_pin
       if old_pin==self.pin:
          new_pin= input('enter the new pin:')
          self.pin=new_pin
       else:
          print('not match pin --oops')
       self.menu()
       
    def check_balance(self):
       pin= input('enter the pin:')
       if self.pin==pin:
           print('your balance is:',self.__balance)
       else:
           print("incorrect pin")
       self.menu()
       
    def withdraw(self):
       pin= input('enter the pin:')
       self.pin=pin
       if self.pin==pin:
           ammount=int(input('enter the withdraw ammount'))
           if ammount<=self.__balance:
               self.__balance= self.__balance-ammount
               print('your total balance:',self.__balance)
           else:
               print("insufficent balance",self.__balance)
       else:
           print('incurrent pin')
       self.menu()
#create object
obj=Atm()

obj.__balance="hehehe" # value not change
print(obj.get_balance()) #value print is 0 (actual value)

print(obj.set_balance('hahahah'))