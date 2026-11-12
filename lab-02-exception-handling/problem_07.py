""" 7. Handle KeyboardInterrupt Exception When Reading Input
       Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
"""
"""
To test this function attempt to cancel your input while the program is running.
"""


def keyboard_interrupt_handler():
    # Implemented a try block to monitor the input operation for KeyboardInterrupt.
    try:
        # Prompts the user to input a number, which will be displayed to the user.
        # Additionally, I converted input to an integer for validation purposes.
        number = int(input("Enter your number, please!: "))
    # Catches KeyboardInterrupt and displays an error message to the user.
    except KeyboardInterrupt:
        print("Please try again, user input was canceled.")
    else:
        # Displays a success message containing the user's provided number.
        print(f"Thank you! The number you entered was {number}")


keyboard_interrupt_handler()
