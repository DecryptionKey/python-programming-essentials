""" Exercise 17. Find the Factorial of a Number
    Write a Python program to calculate the factorial of a given non-negative
    integer.
"""
"""
To test this function, enter a non-negative integer. The program will multiply
the integers from 1 through the entered number and display the factorial.
"""


def calculate_factorial():
    # Implemented a try block to validate that the user's input is an integer.
    try:
        number = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Prevents a factorial calculation for a negative integer.
    if number < 0:
        print("A factorial cannot be calculated for a negative integer.")
        return

    factorial_result = 1

    # Multiplies the running product by every integer from 1 through the number.
    for current_value in range(1, number + 1):
        factorial_result *= current_value

    print(f"The factorial of {number} is {factorial_result}.")


calculate_factorial()
