def Check_Frequency(numbers, target):
    return numbers.count(target)

def main():
    print("Enter the number of elements:")
    size = int(input())

    number = []

    print("Enter the numbers:")
    for _ in range(size):
        number.append(int(input()))

    target = int(input("Enter the number to find frequency: "))

    result = Check_Frequency(number, target)
    print("The frequency of the number is:", result)

if __name__ == "__main__":
    main()