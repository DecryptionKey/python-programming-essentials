""" Exercise 15. Find the Largest and Smallest Digit in a Number
    Write a Python program to find the largest and smallest digit present in a
    given number.
"""
"""
To test this function, enter an integer. The program will examine each digit
and display the largest and smallest digits found.
"""


def find_digit_extremes():
    # Implemented a try block to validate that the user's input is an integer.
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    remaining_number = abs(number)

    # Handles zero because its loop would otherwise have no iterations.
    if remaining_number == 0:
        largest_digit = 0
        smallest_digit = 0
    else:
        # Uses a real digit from the number to initialize both tracked values.
        largest_digit = remaining_number % 10
        smallest_digit = remaining_number % 10

        # Compares every digit with the largest and smallest digits found so far.
        while remaining_number > 0:
            current_digit = remaining_number % 10

            if current_digit > largest_digit:
                largest_digit = current_digit
            elif current_digit < smallest_digit:
                smallest_digit = current_digit

            remaining_number //= 10

    print(f"Largest digit: {largest_digit}")
    print(f"Smallest digit: {smallest_digit}")


find_digit_extremes()
