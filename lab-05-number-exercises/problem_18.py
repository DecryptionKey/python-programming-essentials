""" Exercise 18. Collatz Conjecture
    Write a Python program that repeatedly applies the Collatz rules to a
    positive integer until the number reaches 1.
"""
"""
To test this function, enter a positive integer. The program will display every
value in its Collatz sequence, including the starting number and the final 1.
"""


def display_collatz_sequence():
    # Implemented a try block to validate that the user's input is an integer.
    try:
        number = int(input("Enter a positive integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Prevents values outside the positive range required by the problem.
    if number <= 0:
        print("Please enter an integer greater than 0.")
        return

    collatz_sequence = [number]
    current_number = number

    # Applies the even or odd rule until the current number becomes 1.
    while current_number != 1:
        if current_number % 2 == 0:
            current_number //= 2
        else:
            current_number = current_number * 3 + 1

        collatz_sequence.append(current_number)

    print("Collatz sequence:")
    print(*collatz_sequence, sep=", ")


display_collatz_sequence()
