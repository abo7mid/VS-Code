from BankAccount import BankAccount


class User:
    userid = 0
    def __init__(self,name='',email='',userid=1):
        User.userid += userid
        self.name = name
        self.nickname = ''
        self.email = email
        self.account = BankAccount(0,0)
        self.account.accountNum

        

    
    # def __del__(self):
    #     print("destructor")

    # def openAccount(self):
    #     self.account = BankAccount() 
    
    
    def getUserInfo(self):

        info = {"userid":self.userid,
                "name":self.name,
                "email":self.email,
                "nickname":self.nickname,
                "accountNum":self.account.accountNum
                }
        return info


    def deposit(self,accountNum,amount):
        self.account.deposit(accountNum,amount)
        # we could record the deposited amount



    def withdraw(self,accountNum,amount):
        #if self.account.balance > amount: 
            self.account.withdraw(accountNum,amount)
            # we could record the withdrawn amount


    
    def display_user_balance(self):
        print(f"Hi {self.nickname},{self.name} your balance: {self.account.balance}")







# This is called chaining. In order for this to work, 
# each method must return self. By returning self, 
# if we recall how functions work, 
# each method call will now be equal to the instance that called it.

# For example if A.make_deposit(100) returns its own instance (A), 
# then we can call one of that instance's methods after that call,
#  like A.make_deposit(100).make_withdrawal(50).

# The practice of having OOP return its own instance is pretty common
#  and is done in other programming languages, 
# though the variable name in some languages is not self, but instead this.

# A = User("Ahmed","e515@hotmail.com")
# print(A.getUserInfo())



Ahmed = User("Ahmed","e515@hotmail.com")
Ahmed.display_user_balance()

Muhammed = User('Muhammed','mocob3@gmail.com')
Muhammed.display_user_balance()


Ahmed.deposit(Muhammed.account,500)
Muhammed.display_user_balance()

Ahmed.display_user_balance()
Muhammed.account.transfer_money(Ahmed.account,200)
Muhammed.display_user_balance()

Ahmed.display_user_balance()





# A.account.transfer_money(B,500)














    # def closeAccount(self):
    #     pass
    #     #call the destructor function to close a user account?
    #     self.__del__()
    
    # def suspendAcount(self):
    #     pass

    # def updateAccountInfo(self):
    #     pass

    # def issueCC(self):
    #     pass
    