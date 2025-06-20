def count_occurrences(filename, target):
    try:
        f = open(filename, 'r')         
        content = f.read()            
        f.close()                      
        return content.count(target)   
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return None

def main():
    fname = input("Enter filename: ")
    target = input("Enter string to count: ")
    count = count_occurrences(fname, target)
    if count is not None:
        print(f"'{target}' appears {count} time(s) in '{fname}'.")

if __name__ == "__main__":
    main()
