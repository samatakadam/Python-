from functools import reduce

def get_numbers():
   
    return list(map(int, input("Enter numbers separated by spaces: ").split()))

def filter_numbers(numbers):
   
    return list(filter(lambda x: x < 70 or x > 90, numbers))

def map_numbers(numbers):
    
    return list(map(lambda x: x + 10, numbers))

def reduce_numbers(numbers):
   
    return reduce(lambda x, y: x * y, numbers) if numbers else 0

def main():
    numbers = get_numbers()
    filtered_numbers = filter_numbers(numbers)  
    mapped_numbers = map_numbers(filtered_numbers)  
    product = reduce_numbers(mapped_numbers)  

   
    print("Filtered Numbers:", filtered_numbers)
    print("Mapped Numbers (Increased by 10):", mapped_numbers)
    print("Product of Numbers:", product)

if __name__ == "__main__":
    main()