def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def main():
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    print("Result:", power(base, exponent))

if __name__ == "__main__":
    main()