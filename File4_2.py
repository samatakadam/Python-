def factorial(n):
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_of_factorials(num):
    
    return sum(factorial(i) for i in range(1, num + 1))

def main():
    num = int(input("Enter a number: "))
    print("Sum of factorials:", sum_of_factorials(num))

if __name__ == "__main__":
    main()