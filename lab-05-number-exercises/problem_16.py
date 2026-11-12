""" Exercise 16. Check if a Number Is a Palindrome
    Write a Python program to check whether a given number is a palindrome.
"""
"""
To test this function, enter an integer. The program will reverse its digits
and compare the reversed number with the original number.
"""


def check_number_palindrome():
    # Implemented a try block to validate that the user's input is an integer.
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Negative integers are not treated as palindromes because of their sign.
    if number < 0:
        print(f"{number} is not a palindrome.")
        return

    original_number = number
    remaining_number = number
    reversed_number = 0

    # Reverses a working copy so the original number remains available.
    while remaining_number > 0:
        current_digit = remaining_number % 10
        reversed_number = reversed_number * 10 + current_digit
        remaining_number //= 10

    if original_number == reversed_number:
        print(f"{original_number} is a palindrome.")
    else:
        print(f"{original_number} is not a palindrome.")


check_number_palindrome()
