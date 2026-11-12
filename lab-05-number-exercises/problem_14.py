""" Exercise 14. Reverse an Integer Number
    Write a Python program to reverse a given integer number.
"""
"""
To test this function, enter an integer. The program will reverse its digits
using mathematical operations and display the reversed integer.
"""


def reverse_integer():
    # Implemented a try block to validate that the user's input is an integer.
    try:
        number = int(input("Enter an integer to reverse: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Preserves whether the original integer was negative.
    number_sign = 1

    if number < 0:
        number_sign = -1
    remaining_number = abs(number)
    reversed_number = 0

    # Extracts and adds one digit at a time until no digits remain.
    while remaining_number > 0:
        current_digit = remaining_number % 10
        reversed_number = reversed_number * 10 + current_digit
        remaining_number //= 10

    reversed_number *= number_sign
    print(f"Reversed integer: {reversed_number}")


reverse_integer()
