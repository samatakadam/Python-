def is_prime(num):
   
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
  
    num = int(input("Enter a number: "))
    print(f"{num} is prime!" if is_prime(num) else f"{num} is not prime.")

if __name__ == "__main__":
    main()