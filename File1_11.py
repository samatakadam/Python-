def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n, end="")

def main():
    num = int(input("Enter a number: "))
    print_numbers(num)

if __name__ == "__main__":
    main()