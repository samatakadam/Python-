class BankAccount:
    ROI = 10.5  

    def __init__(self):
        self.Name = input("Enter account holder name: ")
        self.Amount = float(input("Enter initial amount: "))

    def Deposit(self):
        money = float(input(f"{self.Name}, enter amount to deposit: "))
        self.Amount += money

    def Withdraw(self):
        money = float(input(f"{self.Name}, enter amount to withdraw: "))
        if money <= self.Amount:
            self.Amount -= money
        else:
            print("Insufficient funds!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest on", self.Amount, "is", interest)

    def Display(self):
        print("Name:", self.Name)
        print("Balance:", self.Amount)

def main():
    print("\n--- Creating Account 1 ---")
    acc1 = BankAccount()
    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    acc1.CalculateInterest()
    acc1.Display()

    print("\n--- Creating Account 2 ---")
    acc2 = BankAccount()
    acc2.Display()
    acc2.Deposit()
    acc2.Withdraw()
    acc2.CalculateInterest()
    acc2.Display()

if __name__=="_main_":
    main()