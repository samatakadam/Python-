
def Add(num_list):
    total = 0
    for num in num_list:
        total += int(num)
    return total

def main():
    print("Enter the numbers:")
    size=int(input())

    Data=[]

    print("Enter the Values:")
   
    for _ in range(size):
        Data.append(int(input()))

    result=Add(Data)

    print("The sum of all elements is:", result)


if __name__ == "__main__":
    main()


    