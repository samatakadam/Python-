def print_triangle(rows):
   
    for i in range(1, rows + 1):
        print("* " * i)

def main():
    
    rows = int(input("Enter the number of rows: "))
    print_triangle(rows)

if __name__ == "__main__":
    main()