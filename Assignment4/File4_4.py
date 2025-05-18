from functools import reduce

def get_numbers():
   
    return list(map(int, input("Enter numbers separated by spaces: ").split()))

def filter_even_numbers(numbers):
  
    return list(filter(lambda x: x % 2 == 0, numbers))

def square_numbers(numbers):
   
    return list(map(lambda x: x ** 2, numbers))

def sum_numbers(numbers):
   
    return reduce(lambda x, y: x + y, numbers) if numbers else 0

def main():
    numbers = get_numbers()
    even_numbers = filter_even_numbers(numbers)
    squared_numbers = square_numbers(even_numbers)
    total_sum = sum_numbers(squared_numbers)

    print("Even Numbers:", even_numbers)
    print("Squared Numbers:", squared_numbers)
    print("Sum of Squared Numbers:", total_sum)

if __name__ == "__main__":
    main()