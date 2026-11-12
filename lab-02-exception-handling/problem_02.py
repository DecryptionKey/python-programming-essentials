""" 2. Validate Integer Input and Raise ValueError
       Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 
"""
"""
To test this function, attempt to enter any input other than an integer.
"""


def validate_integer():
    # Implemented a try block to monitor the integer conversion for a possible ValueError.
    try:
        # Prompts the user to input an integer, which will be displayed to the user.
        # I converted the input to an integer and used a formatted string for clean output.
        number = int(input("Enter a number, please!: "))
        print(f"Thank you! The number you entered is: {number}.")
    # Implemented an except block to handle ValueError if the input is not an integer.
    except ValueError:
        print("Please, enter a valid integer!")


validate_integer()
