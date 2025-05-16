def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  
        num //= 10  
    return total

def main():
    num = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(num))

if __name__ == "__main__":
    main()