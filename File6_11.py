def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

def main():
    num = int(input("Enter a number: "))
    print("Sum of first", num, "natural numbers:", sum_n(num))

if __name__ == "__main__":
    main()