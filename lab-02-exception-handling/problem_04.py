""" 4. Validate Numerical Inputs and Raise TypeError
       Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
"""
"""
To test this function, attempt to enter any nonnumerical input.
"""

def validate_numbers():
    # Implemented a try block to monitor both float conversions for a possible ValueError.
    try:
        # Prompts the user to input two numbers, which will be displayed to the user.
        # Additionally, I converted both inputs to floats for validation purposes.
        first_number = float(input("Enter your first number, please!: "))
        second_number = float(input("Enter your second number, please!: "))
    # Catches ValueError and raises TypeError; "from None" suppresses the original traceback.
    except ValueError:
        raise TypeError("Please enter a numerical value.") from None
    else:
        # Displays a success message containing both numerical inputs.
        print(
            f"Thank you! The first number you entered was {first_number}"
            f" and second number you entered was {second_number}."
        )


validate_numbers()
