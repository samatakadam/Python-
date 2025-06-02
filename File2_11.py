def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))

if __name__ == "__main__":
    main()