from functools import reduce

def get_numbers():
    
    return list(map(int, input("Enter numbers separated by spaces: ").split()))

def is_prime(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime_numbers(numbers):
    
    return list(filter(lambda x: not is_prime(x), numbers))

def multiply_by_two(numbers):
    
    return list(map(multiply, numbers))

def multiply(n):
    
    return n * 2

def get_maximum(numbers):
   
    return reduce(max, numbers) if numbers else None

def main():
    numbers = get_numbers()
    non_prime_numbers = filter_prime_numbers(numbers)
    multiplied_numbers = multiply_by_two(non_prime_numbers)
    max_number = get_maximum(multiplied_numbers)

    print("Numbers after filtering out primes:", non_prime_numbers)
    print("Numbers after multiplying by 2:", multiplied_numbers)
    print("Maximum number:", max_number)

if __name__ == "__main__":
    main()