import sys

# Function to display contents of the file
def mellow_cat(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # Print each line without adding extra newline
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python mellow_cat.py <filename>")
        return

    filename = sys.argv[1]
    mellow_cat(filename)

if __name__ == "__main__":
    main()
