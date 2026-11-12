""" 8. Handle ArithmeticError Exception in Division
       Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
"""
"""
To test this function attempt to divide any number by zero.
"""


def arithmetic():
    # Implemented a try block to monitor possible input-conversion and division exceptions.
    try:
        # Prompts the user to input a numerator and denominator for the calculation.
        # Additionally, I converted both inputs to integers for validation purposes.
        num = int(input("Enter a numerator, please!: "))
        denom = int(input("Enter a denominator, please!: "))

        # Defined a result variable, which calculates and stores the quotient of the inputs.
        result = num / denom
        print("Results: ", result)
    # Handles ArithmeticError, including ZeroDivisionError when the denominator is zero.
    except ArithmeticError as err:
        print(f"The program has encountered an error: {err}. Please try again.")


# Program header and function call.
print("Welcome to the division calculator!")
print("-----------------------------------")
arithmetic()
