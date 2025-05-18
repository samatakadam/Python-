def is_prime(n):
    if n < 2:  
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")