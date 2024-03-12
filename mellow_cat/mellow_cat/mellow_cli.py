import os
import sys
import colorama
from colorama import Back, Fore, Style

# Initialize Colorama
colorama.init()

# Function to draw 'MC' using Colorama
def draw_mellow():
    print(Back.BLACK + Fore.RED + Style.BRIGHT + r'''
  __  __
 |  \/  | ___ 
 | |\/| |/ _ \
 | |  | |  __/
 |_|  |_|\___| 
''' + Style.RESET_ALL)

# Function to read the contents of a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Function to display half of the file contents
def display_half(file_contents):
    half_index = len(file_contents) // 2
    print(''.join(file_contents[:half_index]))

# Function to count the number of lines in the file
def count_lines(file_contents):
    print(f"Number of lines in the file: {len(file_contents)}")

# Function to list files in the current directory
def list_files():
    files = os.listdir('.')
    for file in files:
        print(file)

# Function to change the current directory
def change_directory(new_dir):
    try:
        os.chdir(new_dir)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory '{new_dir}' not found.")

# Main function
def main():
    draw_mellow()
    print(f"{Fore.YELLOW}Welcome to the Mellow Cat command-line tool!{Style.RESET_ALL}")
    print("You can use this tool to read a file and display its contents.")

    while True:
        command = input(f"{Fore.CYAN}mellowcat>{Style.RESET_ALL} ").strip()
        parts = command.split()

        if not parts:
            continue

        if parts[0] == "mc":
            if len(parts) < 2:
                print("Invalid command. Please provide the 'mc' command followed by the path to the file.")
                continue

            filename = parts[1]
            file_contents = read_file(filename)

            if not file_contents:
                continue

            if '-r' in parts:
                display_half(file_contents)
            elif '-a' in parts:
                count_lines(file_contents)
            else:
                for line in file_contents:
                    print(line.strip())

        elif parts[0] == "dir":
            list_files()

        elif parts[0] == "cd":
            if len(parts) < 2:
                print("Invalid command. Please provide the directory path.")
                continue

            new_dir = ' '.join(parts[1:])
            change_directory(new_dir)

        elif parts[0] == "exit":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
