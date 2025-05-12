def check_number():
    num = int(input("Enter a number: ")) 
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")


check_number()