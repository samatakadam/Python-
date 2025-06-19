import os

def check_file():
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        print("File exists.")
    else:
        print("File not found.")

def main():
    check_file()

if __name__=="_main_":
    main()