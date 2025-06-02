def print_pattern(n, i=1):
    if i > n:
        return
    print("*" * i)  
    print_pattern(n, i + 1)  

def main():
    num = int(input("Enter the number of rows: "))
    print_pattern(num)

if __name__ == "__main__":
    main()