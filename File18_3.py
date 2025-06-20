import sys

def copy_to_demo(src):
    try:
        src_f = open(src, 'r')         
        data = src_f.read()            
        src_f.close()                  

        dst_f = open('Demo.txt', 'w')
        dst_f.write(data)              
        dst_f.close()                  

        print(f"Copied '{src}' → 'Demo.txt'")
    except FileNotFoundError:
        print(f"Error: '{src}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_filename>")
        return
    copy_to_demo(sys.argv[1])

if __name__ == "__main__":
    main()
