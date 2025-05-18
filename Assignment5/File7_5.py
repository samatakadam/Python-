def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    print(f"Area: {calculate_area(length, width)}")
    print(f"Perimeter: {calculate_perimeter(length, width)}")

if __name__ == "__main__":
    main()