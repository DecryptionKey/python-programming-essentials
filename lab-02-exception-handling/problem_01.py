""" 1. Handle ZeroDivisionError Exception
       Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
"""
"""
To test this function, attempt to divide any number by zero.
"""


def division():
    # Implemented a try block to monitor possible input-conversion and division exceptions.
    try:
        # Prompts the user to input a numerator and denominator for the calculation.
        # Additionally, I converted both inputs to integers for validation purposes.
        num = int(input("Enter a numerator, please!: "))
        denom = int(input("Enter a denominator, please!: "))

        # Defined a result variable, which calculates and stores the quotient of the inputs.
        result = num / denom
        print("Results: ", result)
    # Implemented an except block to handle ZeroDivisionError if the denominator is zero.
    except ZeroDivisionError:
        print("Sorry, you can't divide by 0!")


# Program header and function call.
print("Welcome to the division calculator!")
print("-----------------------------------")
division()
