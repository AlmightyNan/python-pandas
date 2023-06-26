import os
import subprocess
from colorama import Fore, Style

def clear_console():
    """Clears the console screen."""

    if os.name == 'nt':  
        os.system('cls')
    elif os.name == 'posix':  
        os.system('clear')
    else:
        print("Unsupported operating system. Run this script in a linux/windows environment.")

class MainModule:
    def main():
        print('''
        Series Object Codes
        1.      Creating a new series object
        2.      Creating series using numpy functions
        3.      Performing operations on series object
        4.      List of numpy functions for a series object
        5.      Slicing elements of a series object
        6.      Sorting series by indexes and data values
        7.      List of attributes for a series object''')
        print()
        username = 'python'  # Replace with the desired username
        pc_name = os.uname().nodename  # Get the current PC name
        current_directory = os.getcwd().split('/')[-1]  # Get the current directory
        option = int(input(f"{Fore.LIGHTGREEN_EX}{username}@{pc_name}:{Fore.LIGHTBLUE_EX}~/{current_directory}{Style.RESET_ALL}$ "))

        if option == 1:
            clear_console()
            other_folder_path = './series'
            python_file = 'create-series.py'

            command = f'python3 {other_folder_path}/{python_file}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()
        
        elif option == 2:
            clear_console()
            path = './series/series-using-np.py'

            command = f'python3 {path}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()

        elif option == 3:
            clear_console()
            path = './series/operations-on-series.py'

            command = f'python3 {path}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()
        
        elif option == 4:
            clear_console()
            path = './series/numpy-functions.py'

            command = f'python3 {path}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()

        elif option == 5:
            clear_console()
            path = './series/series-slicing.py'

            command = f'python3 {path}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()

        elif option == 6:
            clear_console()
            path = './series/sorting-series.py'

            command = f'python3 {path}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()
        
        elif option == 7:
            clear_console()
            path = './series/series-attributes.py'

            command = f'python3 {path}'
            process = subprocess.call(command, shell=True)
            print()

            x = input("Press enter to go back to the prompt...")
            if (x):
                process.terminate()

while True:
    clear_console()
    MainModule.main()