def double_numbers(numbers):
    
    def double(x):
        return x * 2  
    
    return list(map(double, numbers))  

def main():
   
    n = int(input("Enter the number of elements: "))
    numbers = []  

    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    doubled_list = double_numbers(numbers)
    print(f"Doubled numbers: {doubled_list}")


if __name__ == "__main__":
    main()