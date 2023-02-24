import os

from lib import file_operations, time, contact
from helpers import help, banner

prompt = 'guest@pypmpte'
NAME = "PyPrompter"
VERSION_TAG = "v0.01 alpha"

commands = {
    
}

command = ''
exit_commands = ['exit']
retCode = 100



banner()

while True:
    current_time = time.currentTime(12)[0]
    command = input(f"{prompt}-({current_time})>> ")
    if command == "":
        continue

    args = command.split()
    
    if args[0] == "exit":
        break

    elif args[0] == "$":
        print("STATUS -> ", end='')
        print(retCode)
    
    elif args[0] == "clear":
        if os.name == "nt":
            os.system("cls")
            retCode = 0
        else:
            os.system("clear")
            retCode = 0
    
    elif args[0] == "help":
        help()
        retCode = 0

    # Basic Operations
    elif args[0] == "ls":
        try:
            print(os.listdir(os.getcwd()))
            retCode = 0
        except:
            print("Error: Unable to list directory")
            retCode = -1
    
    elif args[0] == "mkdir":
        try:
            os.mkdir(args[1])
            retCode = 0
        except:
            print("Error: Invalid directory name")
            retCode = -1

    elif args[0] == "rmdir":
        try:
            os.rmdir(args[1])
            retCode = 0
        except:
            print("Error: Invalid directory name")
            retCode = -1

    elif args[0] == "cd":
        try:
            os.chdir(args[1])
            retCode = 0
        except:
            print("Error: Invalid path")
            retCode = -1

    # File Operations
    elif args[0] == "create":
        filename = args[1]
        try:
            content = args[2]
        except:
            content = "pyprompter" + str(time.currentTime(24, True, True, True))
        try:
            file_operations.create(filename)
            retCode = 0
        except:
            print("Error: Wrong file name")
            retCode = -1

    # Set Shell Variables
    elif args[0] == "var":
        try:
            var_name = args[1]
            var_value = args[2]
            os.environ[var_name] = var_value
            retCode = 0
        except e:
            print("Error: Invalid command syntax", e)
            retCode = -1

    elif args[0] == "print":
        try:
            print(os.environ[args[1]])
            retCode = 0
        except:
            print("Error: Invalid variable name")
            retCode = -1
    
    elif args[0] == "contact":
        result = contact.returnContact() 
        retCode = result[1]
        print(result[0])

    

    

print("Exiting Shell")