from functools import reduce

def main():
    
    numbers = []
    n = int(input("Enter the number of elements in the list: "))

    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

  
    filtered_numbers = list(filter(lambda x: 70 <= x <= 90, numbers))
    
   
    mapped_numbers = list(map(lambda x: x + 10, filtered_numbers))
    
   
    result = reduce(lambda x, y: x * y, mapped_numbers)

 
    print("List after filter:", filtered_numbers)
    print("List after map:", mapped_numbers)
    print("Output of reduce:", result)


if __name__ == "__main__":
    main()