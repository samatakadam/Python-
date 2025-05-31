import threading

def evenlist(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    print(f"Sum of even numbers: {sum_even}")

def oddlist(numbers):
    sum_odd = 0
    for num in numbers:
        if num % 2 != 0:
            sum_odd += num
    print(f"Sum of odd numbers: {sum_odd}")

try:
    input_str = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, input_str.strip().split()))
    
    
    even_thread = threading.Thread(target=evenlist, args=(numbers,))
    odd_thread = threading.Thread(target=oddlist, args=(numbers,))

  
    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Finished processing the list.")
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
