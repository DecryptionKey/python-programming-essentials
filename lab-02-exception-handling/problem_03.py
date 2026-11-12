""" 3. Handle FileNotFoundError Exception When Opening a File
       Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""
"""
To test this function, change the filename to one that does not exist in this
directory or project. The exception will then be handled correctly.
"""


def file_open(file_path):
    # Implemented a try block to monitor the file-opening operation for an exception.
    try:
        # Implemented with open in read mode to read the file at the provided path.
        with open(file_path, "r") as file:
            print(file.read())
    # Implemented an except block to handle FileNotFoundError if the path does not exist.
    except FileNotFoundError:
        print("File Not Found. Please try again.")


file_open("file_not_found_test.txt")
