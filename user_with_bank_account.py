class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
account1 = BankAccount(0.01, 100)
account2 = BankAccount(0.02, 200)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit (amount)
        return self

    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self

    def display_account_info(self):
        self.account.display_account_info()
        return self
    
user1 = User("zara", "zara@gmail.com")
user1.make_deposit(30).make_withdraw(15).display_account_info()