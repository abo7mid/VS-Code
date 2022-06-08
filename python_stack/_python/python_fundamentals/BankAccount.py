from code import interact


class BankAccount:

    def __init__(self,int_rate=0,balance=0):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        return self


    def withdraw(self,amount):
        if self.balance < amount:
            print("insufficient funds: Chagring a $5 fee")
            self.balance -= 5
        self.balance -= amount
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


account1 = BankAccount(0.01,500).deposit(100).withdraw(599).display_account_info().yield_interest()

account2 = BankAccount(0.01,0)

account2.deposit(100).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(0).yield_interest().display_account_info()