def show_file(name):
    try:
        f = open(name, 'r')
        print("\nFile Contents:\n")
        print(f.read())
        f.close()
    except:
        print("File not found.")

def main():
    fname = input("Enter file name: ")
    show_file(fname)

if __name__=="_main_":
    main()