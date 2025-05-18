def is_palindrome(s):
    
    s = s.lower().replace(" ", "")  
    reversed_s = "" 

   
    for char in s:
        reversed_s = char + reversed_s

    return s == reversed_s 

def main():
    
    text = input("Enter a string: ")
    if is_palindrome(text):
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')


if __name__ == "__main__":
    main()