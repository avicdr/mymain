import os
import random
from datetime import datetime
import time

def append_text_to_file(filename):
    """
    Appends random text with a timestamp to the specified file.
    """
    random_text = ["Hello, World!", "Python is awesome!", "This is random text.", "Have a great day!", "Automated update"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text_to_add = f"[{timestamp}] {random.choice(random_text)}\n"

    with open(filename, 'a') as file:
        file.write(text_to_add)
        print(f"Appended to {filename}: {text_to_add.strip()}")

def execute_terminal_command(command):
    """
    Executes a terminal command.
    """
    print(f"Executing command: {command}")
    os.system(command)

if __name__ == "__main__":
    # File to edit
    filename = "init.txt"

    # Check if the file exists, if not, create it
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("Initial file created.\n")
            print(f"File {filename} created.")

    # Append text with timestamp
    append_text_to_file(filename)

    # Run a terminal command
    execute_terminal_command("cd D:\Code\codePusher")
    time.sleep(1)
    execute_terminal_command(f'git commit -m {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Commit')
    time.sleep(1)
    execute_terminal_command("git push -u origin main")