def is_prime(n):
   
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):

    return list(filter(is_prime, numbers))

def main():
    
    n = int(input("Enter the number of elements: "))
    numbers = [] 

    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    prime_numbers = filter_primes(numbers)
    print(f"Prime numbers: {prime_numbers}")


if __name__ == "__main__":
    main()