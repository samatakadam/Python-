def print_table(num):
    i = 1
    while i <= 10:
        print(num, "x", i, "=", num * i)
        i += 1

def main():
    num = int(input("Enter a number: "))
    print_table(num)

if __name__ == "__main__":
    main()