import os
import shutil
import subprocess
import sys
import colorama
import requests
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
    files = os.listdir('../../AppData/Roaming/JetBrains/PyCharmCE2023.3/scratches')
    for file in files:
        print(file)


# Function to change the current directory
def change_directory(new_dir):
    try:
        os.chdir(new_dir)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory '{new_dir}' not found.")


# Function to display current directory
def print_current_directory():
    print(f"Current directory: {os.getcwd()}")


# Function to create a new directory
def make_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")


# Function to remove a directory
def remove_directory(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' removed.")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found.")


# Function to remove a file
def remove_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


# Function to copy a file
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"File '{src}' copied to '{dest}'.")
    except FileNotFoundError:
        print(f"File '{src}' not found.")


# Function to move a file
def move_file(src, dest):
    try:
        shutil.move(src, dest)
        print(f"File '{src}' moved to '{dest}'.")
    except FileNotFoundError:
        print(f"File '{src}' not found.")


# Function to change file ownership
def change_ownership(file_name, owner):
    try:
        os.chown(file_name, owner)
        print(f"Ownership of '{file_name}' changed to '{owner}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


# Function to print current user
def print_current_user():
    print(f"Current user: {os.getlogin()}")


# Function to print current date and time
def print_current_datetime():
    from datetime import datetime
    print(f"Current date and time: {datetime.now()}")


# Function to print help information
def print_help():
    print("Available commands:")
    print("dir/ls - List files in the current directory")
    print("cd <directory> - Change directory")
    print("pwd - Print current directory")
    print("mkdir <directory> - Create a new directory")
    print("rmdir <directory> - Remove a directory")
    print("del <file> - Delete a file")
    print("copy <source> <destination> - Copy a file")
    print("move <source> <destination> - Move a file")
    print("chown <file> <owner> - Change file ownership")
    print("whoami - Print current user")
    print("date - Print current date and time")
    print("python - Launch Python interpreter")
    print("echo <message> - Print a message")
    print("help - Print help information")
    print("mc <file> [-r] [-a] - Read a file")
    print("mcweb <url> - Read text from a URL")
    print("exit - Exit the Mellow Cat shell")


# Function to read text from a URL
def read_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Error fetching text from URL: {e}")
        return []
# Function to read text from a URL using curl
def read_text_from_url_curl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching text from URL: {e}")
        return ""

# Function to print text from a URL
def print_text_from_url(url, use_curl=False):
    if use_curl:
        text = read_text_from_url_curl(url)
    else:
        text = '\n'.join(read_text_from_url(url))
    print(text)

# Main function
def main():
    draw_mellow()
    print(f"{Fore.YELLOW}Welcome to the Mellow Cat command-line tool!{Style.RESET_ALL}")
    print("You can use this tool to perform various file system operations.")

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

        elif parts[0] == "dir" or parts[0] == "ls":
            list_files()

        elif parts[0] == "cd":
            if len(parts) < 2:
                print("Invalid command. Please provide the directory path.")
                continue

            new_dir = ' '.join(parts[1:])
            change_directory(new_dir)

        elif parts[0] == "pwd":
            print_current_directory()

        elif parts[0] == "mkdir":
            if len(parts) < 2:
                print("Invalid command. Please provide the directory name.")
                continue

            dir_name = ' '.join(parts[1:])
            make_directory(dir_name)

        elif parts[0] == "rmdir":
            if len(parts) < 2:
                print("Invalid command. Please provide the directory name.")
                continue

            dir_name = ' '.join(parts[1:])
            remove_directory(dir_name)

        elif parts[0] == "del":
            if len(parts) < 2:
                print("Invalid command. Please provide the file name.")
                continue

            file_name = ' '.join(parts[1:])
            remove_file(file_name)

        elif parts[0] == "copy":
            if len(parts) < 3:
                print("Invalid command. Please provide source and destination.")
                continue

            src = parts[1]
            dest = parts[2]
            copy_file(src, dest)

        elif parts[0] == "move":
            if len(parts) < 3:
                print("Invalid command. Please provide source and destination.")
                continue

            src = parts[1]
            dest = parts[2]
            move_file(src, dest)

        elif parts[0] == "chown":
            if len(parts) < 3:
                print("Invalid command. Please provide file and owner.")
                continue

            file_name = parts[1]
            owner = parts[2]
            change_ownership(file_name, owner)

        elif parts[0] == "whoami":
            print_current_user()

        elif parts[0] == "date":
            print_current_datetime()

        elif parts[0] == "python":
            subprocess.run(["python"])

        elif parts[0] == "echo":
            message = ' '.join(parts[1:])
            print(message)

        elif parts[0] == "help":
            print_help()

        elif parts[0] == "mcweb":
            if len(parts) < 2:
                print("Invalid command. Please provide the URL.")
                continue

            url = parts[1]
            print_text_from_url(url, use_curl=True)
            file_contents = read_text_from_url(url)

            if not file_contents:
                print("Failed to fetch text from URL.")
                continue

            for line in file_contents:
                print(line.strip())

        elif parts[0] == "exit":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
