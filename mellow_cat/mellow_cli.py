import time
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display loading animation
def loading_animation():
    for _ in range(3):
        print("Loading.", end="\r")
        time.sleep(0.5)
        print("Loading..", end="\r")
        time.sleep(0.5)
        print("Loading...", end="\r")
        time.sleep(0.5)

# Function to display the startup sequence
def startup_sequence():
    clear_screen()
    print(r"""
        _____      _                
       / ____|    (_)               
      | |     _ __ _ _ __ ___   ____
      | |    | '__| | '_ ` _ \ / _  |
      | |____| |  | | | | | | | (_| |
       \_____|_|  |_|_| |_| |_|\__,_|
    """)
    loading_animation()
    clear_screen()
    print("Welcome to Mellow!")
    print("Type 'help' for a list of available commands.")
    print("")

# Main function
def main():
    startup_sequence()
    while True:
        command = input("Mellow> ")
        # Handle commands here...

if __name__ == "__main__":
    main()
