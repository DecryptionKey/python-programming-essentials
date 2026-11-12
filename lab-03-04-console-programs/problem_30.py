""" P-1.30 Repeated Division by Two
    Write a Python program that can take a positive integer greater than 2 as
    input and write out the number of times one must repeatedly divide this
    number by 2 before getting a value less than 2.
"""
"""
To test this function, enter a positive integer greater than 2. The program
will repeatedly divide the value by 2 and display the number of divisions.
"""


def repeated_division():
    # Implemented a try block to validate that the user's input is an integer.
    try:
        number = int(input("Enter a positive integer greater than 2: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Implemented a decision structure to enforce the required input range.
    if number <= 2:
        print("Please enter a positive integer greater than 2.")
        return

    # Created a counter to track how many divisions are performed.
    division_count = 0
    current_value = number

    # Repeatedly divides the current value until it becomes less than 2.
    while current_value >= 2:
        current_value /= 2
        division_count += 1

    print(
        f"The number {number} must be divided by 2 a total of "
        f"{division_count} time(s) before becoming less than 2."
    )


repeated_division()
