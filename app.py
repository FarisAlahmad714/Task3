class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon

    def account_info(self):
        print(f"Interest Rate: {self.int_rate}")
        print(f"Balance: {self.balance}")
        return self    

    def deposit(self, amount):
        self.balance += amount
        print("\n Amount Deposited:",amount)
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")
        return self
    
    def display_account_info(self):
        print("\n Net Available balance=",self.balance)
        return self
    
    def yield_interest(self):
        amount = self.balance * self.int_rate
        newYield = self.balance + amount
        self.balance = newYield
        print("\n New balance w/ interest: ",self.balance)
        return self

    @classmethod
    def bank_account_info(cls):
        for bank in cls.all_accounts:
            print(bank.account_info())

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checking":BankAccount(int_rate=0.02, balance=0)}

    def make_Account(self, name, bankAccount):
        self.account[name] = bankAccount

    #other methods
    def make_deposit(self, name, amount):
        self.account[name].deposit(amount)
        self.account[name]
        print(self.account[name].balance)
        return self

    def make_withdraw(self, name, amount):
        self.account[name].withdraw(amount)
        print(self.account[name].balance)
        return self

    def display_user_balance(self, name):
        print("Net Balance: ",self.account[name].balance)


user1 = User('Judah', 'jmendoza@gmail.com')
user1.make_Account('savings', BankAccount(0.10, 5000))
user1.make_Account('checking',BankAccount(0.07, 2500))
user1.make_deposit('savings', 750).make_withdraw('savings', 3000).display_user_balance('savings')
user1.make_deposit('checking', 1000).make_withdraw('checking', 500).display_user_balance('checking')
user1.display_user_balance('savings')
user1.display_user_balance('checking')