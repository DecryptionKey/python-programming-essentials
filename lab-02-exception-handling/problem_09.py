""" 9. Handle UnicodeDecodeError When Opening a File
       Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
"""
"""
To test this function, I've created two test files: "utf16be.txt" and "utf8.txt".
I've set one file to UTF-16BE and the other to UTF-8. The file "utf8.txt" should
open and display its contents successfully because the program uses UTF-8. The
other file should trigger the exception because the program cannot decode it.
"""


def unicode_decode_error(file_path):
    # Implemented a try block to monitor the file-opening operation for a possible exception.
    try:
        # Used with open in read mode and UTF-8 to read the file at the provided path.
        with open(file_path, "r", encoding="utf-8") as file:
            print(file.read())
    # Handles UnicodeDecodeError if the file's contents cannot be decoded as UTF-8.
    except UnicodeDecodeError as ude:
        print("Encoding error: the file's content could not be decoded as UTF-8.")
        print(ude)


unicode_decode_error("utf16be.txt")
unicode_decode_error("utf8.txt")
