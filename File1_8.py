import threading

def print_even():
    for i in range(2, 21, 2):  
        print(f"Even: {i}")

def print_odd():
    for i in range(1, 20, 2):  
        print(f"Odd: {i}")


even_thread = threading.Thread(target=print_even, name="EvenThread")
odd_thread = threading.Thread(target=print_odd, name="OddThread")


even_thread.start()
odd_thread.start()


even_thread.join()
odd_thread.join()

print("Finished printing even and odd numbers.")
