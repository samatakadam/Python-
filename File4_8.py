import threading

def count_lowercase(s):
    count = 0
    for c in s:
        if c.islower():
            count += 1
    thread = threading.current_thread()
    print(f"[{thread.name} | ID: {thread.ident}] Lowercase letters: {count}")

def count_uppercase(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    thread = threading.current_thread()
    print(f"[{thread.name} | ID: {thread.ident}] Uppercase letters: {count}")

def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1
    thread = threading.current_thread()
    print(f"[{thread.name} | ID: {thread.ident}] Digits: {count}")

def main():
    input_str = input("Enter a string: ")

   
    small_thread = threading.Thread(target=count_lowercase, args=(input_str,), name='small')
    capital_thread = threading.Thread(target=count_uppercase, args=(input_str,), name='capital')
    digits_thread = threading.Thread(target=count_digits, args=(input_str,), name='digits')

  
    small_thread.start()
    capital_thread.start()
    digits_thread.start()

 
    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Main thread exiting.")

if __name__ == "__main__":
    main()
