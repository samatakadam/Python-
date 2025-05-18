def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2 if num2 != 0 else "Cannot divide by zero"

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Sum:", add(num1, num2))
    print("Difference:", subtract(num1, num2))
    print("Product:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

if __name__ == "__main__":
    main()