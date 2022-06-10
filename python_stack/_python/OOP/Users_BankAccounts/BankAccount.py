

class BankAccount:
    accountNum = 0
    def __init__(self,int_rate=0.0,balance=0,accountNum=1):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accountNum += accountNum


    def deposit(self,accountNum,amount):
        accountNum.balance += amount
        self.sendSMS(f"{amount} has been deposited to your account")
        return self



    # Making this function run every time a transection is made 
    # (withdrawal,deposit,transfer,online payment etc)
    def sendSMS(self,message):
        print(message)




    def withdraw(self,accountNum,amount):
        if accountNum.balance < amount:
            print("insufficient funds: Chagring a $5 fee")
            self.balance -= 5
        self.sendSMS(f"{amount} has been deducted from your account")
        accountNum.balance -= amount
        return self


        
    def transfer_money(self,beneficiary,amount):
        if(self.balance > amount):
            self.balance -= amount
            beneficiary.balance = beneficiary.balance + amount
            print(f"A transection has been made to {beneficiary}")
        return self


    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self


    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            print(f"your balance with interest ${interest}")
        else:
            print(f"insufficient funds to calculate the interest ${self.balance}")
        return self


