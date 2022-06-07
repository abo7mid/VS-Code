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
        pass

    def make_withdrawal(self,amount):
        if(self.balance>amount):
            self.balance -= amount
        else:
            print(f"You do not have enough money for this transection Mr {self.name}")

    def display_user_balance(self):
        print(f"Hi, Mr {self.name} your balance is {self.balance}$")


    def transfer_money(self,beneficiary,amount):
        self.balance -= amount
        beneficiary.balance = beneficiary.balance + amount


    def sendSMS(self,PhoneNum):  
        pass
        # Making this function run every time a transection is made 
        # (withdrawal,deposit,transfer,online payment etc)


A = User("A",1000)
A.display_user_balance()


B = User("B",1000)
B.display_user_balance()

C = User("C",1000)
C.display_user_balance()

A.transfer_money(B,500)

A.display_user_balance()
B.display_user_balance()

