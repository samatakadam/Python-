import threading

def evenfactor(n):
    sum_even = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            sum_even += i
    print(f"Sum of even factors of {n}: {sum_even}")

def oddfactor(n):
    sum_odd = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            sum_odd += i
    print(f"Sum of odd factors of {n}: {sum_odd}")


try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
       
        even_thread = threading.Thread(target=evenfactor, args=(number,))
        odd_thread = threading.Thread(target=oddfactor, args=(number,))

       
        even_thread.start()
        odd_thread.start()

       
        even_thread.join()
        odd_thread.join()

        print("exit from main")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
