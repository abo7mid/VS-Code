class User:

    def __init__(self,name='',balance=0,userid=1):
        self.userid = userid 
        self.balance = balance
        self.name = name
        self.accountNumber = balance
        self.nickname = ''
        self.email = ''
    
    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        if(self.balance>amount):
            self.balance -= amount
        else:
            print(f"You do not have enough money for this transection Mr {self.name}")

    def display_user_balance(self):
        print(f"Hi, Mr {self.name} your balance is {self.balance}$")
        return self



    def transfer_money(self,beneficiary,amount):
        self.balance -= amount
        beneficiary.balance = beneficiary.balance + amount
        return self



    def sendSMS(self,PhoneNum):  
        return self

        # Making this function run every time a transection is made 
        # (withdrawal,deposit,transfer,online payment etc)






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

A = User("A",1000).display_user_balance()

B = User("B",1000).display_user_balance()

C = User("C",1000).display_user_balance()

A.transfer_money(B,500).display_user_balance()

B.display_user_balance()

