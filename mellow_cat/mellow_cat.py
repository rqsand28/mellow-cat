import sys


# Function to display contents of the file
def mellow_cat(filename, preview=False, short_desc=False):
    try:
        with open(filename, 'r') as file:
            if preview:
                print("Preview of text:")
                for _ in range(5):  # Display only the first 5 lines
                    print(file.readline().strip())
            else:
                for line in file:
                    print(line, end='')  # Print each line without adding extra newline
            if short_desc:
                print("\nShort description:")
                print("This is a server log file.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


# Main function
def main():
    if len(sys.argv) < 2 or '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: python mellow_cat.py <filename> [-r] [-a]")
        print("-r : Preview the text")
        print("-a : Show a short description of the text")
        return

    filename = sys.argv[1]
    preview = '-r' in sys.argv
    short_desc = '-a' in sys.argv
    mellow_cat(filename, preview, short_desc)


if __name__ == "__main__":
    main()
