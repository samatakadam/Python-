class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    calc = Calculator(a, b)

    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())

if __name__=="_main_":
    main()