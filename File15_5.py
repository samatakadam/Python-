def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        with open(filename, 'r') as file:
            text = file.read()
            count = text.count(word)
            print(f"The word '{word}' appears {count} times.")
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()
