""" P-1.32 Console Calculator
    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. Each input to the
    calculator, whether a number such as 12.34 or 1034, or an operator such as
    + or =, should be entered on a separate line. After each input, output to the
    Python console what would be displayed on the calculator.
"""
"""
To test this function, enter a number, an arithmetic operator, another number,
and then an equals sign. Enter "q" at any time to exit the calculator.

Ex:
----------
Input: 12
Input: +
Input: 3
Input: =

"""


def console_calculator():
    # Created variables to store the calculator's display and pending operation.
    display_value = 0.0
    stored_value = None
    pending_operator = None
    expecting_number = True

    print("Calculator App")
    print('Enter numbers and operators on separate lines. Enter "q" to quit.')
    print("Display:", display_value)

    # Continues accepting calculator input until the user chooses to quit.
    while True:
        user_input = input("Input: ")

        if user_input == "q":
            print("Calculator closed.")
            break

        if expecting_number:
            # Attempts to convert the current input into a numerical value.
            try:
                display_value = float(user_input)
            except ValueError:
                print("Please enter a valid number.")
                print("Display:", display_value)
                continue

            if stored_value is None:
                stored_value = display_value

            expecting_number = False
            print("Display:", display_value)
            continue

        if user_input in ("+", "-", "*", "/"):
            # Stores the chosen arithmetic operation until another number is entered.
            if pending_operator is None:
                stored_value = display_value
            pending_operator = user_input
            expecting_number = True
            print("Display:", display_value)
            continue

        if user_input == "=":
            # Performs the pending calculation when both numbers are available.
            if pending_operator is not None and stored_value is not None:
                try:
                    if pending_operator == "+":
                        display_value = stored_value + display_value
                    elif pending_operator == "-":
                        display_value = stored_value - display_value
                    elif pending_operator == "*":
                        display_value = stored_value * display_value
                    elif pending_operator == "/":
                        display_value = stored_value / display_value
                except ZeroDivisionError:
                    print("Error: division by zero is not allowed.")
                    display_value = 0.0

                stored_value = display_value
                pending_operator = None

            print("Display:", display_value)
            continue

        # If a number has already been entered, only an operator or equals is valid.
        print("Please enter +, -, *, /, =, or q.")
        print("Display:", display_value)


console_calculator()
