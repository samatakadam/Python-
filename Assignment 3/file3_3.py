def find_minimum(numbers):
    
    mini_num = numbers[0]  
    for num in numbers:
        if num < mini_num:
            mini_num = num  
    return mini_num

def main():
   
    print("Enter the number of elements:")
    size = int(input())

    numbers = []  

    print("Enter the values:")
    
    for _ in range(size):
        numbers.append(int(input()))  
    result = find_minimum(numbers)  
    print("The maximum number is:", result)


if __name__ == "__main__":
    main()