""" 5. Handle PermissionError Exception When Opening a File
       Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
"""
"""
To test this function, attempt to open any file without read permissions.
"""

def permission_error(file_path):
    # Implemented a try block to monitor the file-opening operation for an exception.
    try:
        # Implemented with open in read mode to read the file at the provided path.
        with open(file_path, "r") as file:
            print(file.read())
    # Implemented an except block to handle PermissionError if read permission is denied.
    except PermissionError:
        print("Permission denied")

# Temporarily remove this test file's read permission to test the PermissionError handler.
permission_error("permission_test.txt")
