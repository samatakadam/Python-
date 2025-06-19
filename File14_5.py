class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.account_number = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)

def main():
    acc1 = BankAccount(101, "Priya", 1000)
    acc1.display()
    acc1.deposit(500)
    acc1.withdraw(300)
    acc1.display()

if __name__=="_main_":
    main()