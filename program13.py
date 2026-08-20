class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"Account: {self.__account_number}")
        print(f"Name: {self.__name}")
        print(f"Balance: ₹{self.__balance}")


# --------------------------------
# Savings Account
# --------------------------------

class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, balance=0, interest_rate=0.04):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        # Savings account cannot withdraw more than balance
        print("Savings Account:")
        super().withdraw(amount)

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ₹{interest:.2f}")


# --------------------------------
# Current Account
# --------------------------------

class CurrentAccount(BankAccount):
    def __init__(self, account_number, name, balance=0, overdraft=5000):
        super().__init__(account_number, name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        # Current account allows overdraft
        if amount <= self.get_balance() + self.overdraft:
            print("Current Account:")
            super().withdraw(amount)

            # Handle overdraft separately
            if amount > self.get_balance():
                print("Overdraft facility used.")
        else:
            print("Overdraft limit exceeded.")


# --------------------------------
# Polymorphism
# --------------------------------

accounts = [
    SavingsAccount("SA101", "Rahul", 10000),
    CurrentAccount("CA201", "Amit", 5000)
]

for account in accounts:
    account.display()

    account.deposit(1000)
    account.withdraw(3000)

    print("Current Balance:", account.get_balance())
    print()
