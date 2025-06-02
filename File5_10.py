from functools import reduce


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def multiply_by_two(n):
    return n * 2

def main():
  
    numbers = []
    n = int(input("Enter the number of elements in the list: "))

    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

   
    filtered_numbers = list(filter(is_prime, numbers))
    
    
    mapped_numbers = list(map(multiply_by_two, filtered_numbers))
    
   
    result = reduce(lambda x, y: max(x, y), mapped_numbers)

   
    print("List after filter:", filtered_numbers)
    print("List after map:", mapped_numbers)
    print("Output of reduce:", result)


if __name__ == "__main__":
    main()