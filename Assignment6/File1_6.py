class NumberPrinter:
    
    def print_numbers():
        num = 1
        while num <= 50:
            print(num, end=" ")
            num += 1

def main():
    print("Numbers from 1 to 50:")
    NumberPrinter.print_numbers()

if __name__ == "__main__":
    main()