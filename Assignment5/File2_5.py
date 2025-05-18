def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def check_character(char):
    if is_vowel(char):
        print(f"{char} is a Vowel.")
    else:
        print(f"{char} is a Consonant.")

def main():
    char = input("Enter a single character: ")
    
    if len(char) == 1 and char.isalpha():
        check_character(char)
    else:
        print("Invalid input! Please enter a single letter.")

if __name__ == "__main__":
    main()