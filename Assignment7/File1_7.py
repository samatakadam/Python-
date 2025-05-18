

def square(num):
   
    return (lambda x: x ** 2)(num)

def cube(num):
   
    return (lambda x: x ** 3)(num)

def main():

    num = int(input("Enter a number: "))
    print(f"Square of {num}: {square(num)}")
    print(f"Cube of {num}: {cube(num)}")


if __name__ == "__main__":
    main()