

def multiply():
    return lambda a, b: a * b

def main():
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    
    multiplication = multiply()
    result = multiplication(num1, num2)

    
    print("Multiplication result:", result)

if __name__ == "__main__":
    main()