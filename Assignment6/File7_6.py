def find_largest(numbers):
    
    return max(numbers) 

def main():
    
    n = int(input("Enter the number of elements: "))
    numbers = []  

    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    largest = find_largest(numbers)
    print(f"The largest number is: {largest}")


if __name__ == "__main__":
    main()