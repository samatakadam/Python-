def count_zeros(n):
    if n == 0:
        return 1  
    if n < 10:
        return 0 
    return (1 if n % 10 == 0 else 0) + count_zeros(n // 10)

def main():
    num = int(input("Enter a number: "))
    print("Number of zeros:", count_zeros(num))

if __name__ == "__main__":
    main()
