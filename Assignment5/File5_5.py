def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

def main():
    num = int(input("Enter a number: "))
    check_even_odd(num)

if __name__ == "__main__":
    main()