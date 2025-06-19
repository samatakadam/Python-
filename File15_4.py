import sys


def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1:
            data1 = f1.read()

        with open(file2, 'r') as f2:
            data2 = f2.read()

        if data1 == data2:
            return True
        else:
            return False

    except FileNotFoundError:
        print("One or both files not found.")
        return False

def main():
    if len(sys.argv) != 3:
        print("Please give two file names.")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if compare_files(file1, file2):
        print("Success: Files are same.")
    else:
        print("Failure: Files are different.")


if __name__ == "__main__":
    main()
