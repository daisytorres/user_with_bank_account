class BankAccount:
    # all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        self.acc_type = acc_type
        BankAccount.all_accounts.append(self)

# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

#withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging $5 fee")
            self.balance -= 5
        return self

#display_account_info(self) - print to the console: 
    def display_account_info(self):
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: {self.balance}")
        return self

# increases balance by balance* interest rate if balance is greater than 0
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+ self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.01, balance = 0)

    def make_deposit (self, amount):
        self.account.deposit(amount)
        print(f"You made a deposit of {amount}")
        return self
    
    def withdrawal_amount (self, amount):
        self.account.withdrawal (amount)
        print(f"You took out {amount}")
        return self
    
    def display(self):
        self.account.display_account_info()
        print(self.name)
        print(self.email)
        print(f"Your account balance is {self.account.balance}")
        return self
    
account_holder = User("Daisy", "daisy@fake.com")
print(account_holder.withdrawal_amount(500))