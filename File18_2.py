def show_file(fname):
    
    try:
        f = open(fname, "r")         
        data = f.read()               
        print(data, end="")         
        f.close()                   
    except FileNotFoundError:
        print(f"Error: '{fname}' not found.")

def main():
    fname = input("Enter filename: ")
    show_file(fname)


if __name__ == "__main__":
    main()
