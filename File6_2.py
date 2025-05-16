def print_pattern(rows):
    
    for i in range(rows, 0, -1):
        print("*" * i)

def main():
    
    n = int(input("Enter the number of rows: "))
    print_pattern(n)

if __name__ == "__main__":
    main()