def Calculate_Power():
   
    return lambda n: 2 ** n

def main():

 Data= int(input("Enter a number: "))
 power_of_2 = Calculate_Power()
 result = power_of_2(Data)

 print("Power of 2 of number is:", result)


if __name__ == "__main__":
    main()