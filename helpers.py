import pyfiglet

NAME = "PyPrompter"
VERSION_TAG = "v0.01 alpha"

def help():
    data = [
        ["(dir, mkdir, rmdir)", "basic filesystem manipulations"],
        ["contact", "contact the author of the project"],
        ["create", "create a file"]
    ]

    print()

    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print("".join(word.ljust(col_width) for word in row))
    
    print()


def banner():
    ascii_art = pyfiglet.figlet_format(NAME, font = "slant")
    print(f"Copyright © {NAME} {VERSION_TAG} free and open shell")
    print(ascii_art)
    print("Welcome to interactive python terminal.")