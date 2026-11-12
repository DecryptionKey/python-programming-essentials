""" P-1.31 Make Change
    Write a Python program that can "make change." Your program should take two
    numbers as input, one that is a monetary amount charged and the other that
    is a monetary amount given. It should then return the number of each kind of
    bill and coin to give back as change for the difference between the amount
    given and the amount charged. The values assigned to the bills and coins can
    be based on the monetary system of any current or former government. Try to
    design your program so that it returns as few bills and coins as possible.
"""
"""
To test this function, enter an amount charged and a larger amount given. The
program uses United States currency and returns the fewest bills and coins.
"""


def make_change():
    # Implemented a try block to validate both monetary inputs as numbers.
    try:
        amount_charged = float(input("Enter the monetary amount charged: $"))
        amount_given = float(input("Enter the monetary amount given: $"))
    except ValueError:
        print("Please enter valid numerical monetary amounts.")
        return

    # Prevents negative amounts and payments smaller than the amount charged.
    if amount_charged < 0 or amount_given < 0:
        print("Monetary amounts cannot be negative.")
        return
    if amount_given < amount_charged:
        print("The amount given is not enough to cover the amount charged.")
        return

    # Converts both monetary amounts to cents to avoid floating-point errors.
    charged_in_cents = round(amount_charged * 100)
    given_in_cents = round(amount_given * 100)
    remaining_change = given_in_cents - charged_in_cents
    total_change = remaining_change

    # Stores United States denominations from greatest to least value.
    denominations = [
        (10000, "$100 bill"),
        (5000, "$50 bill"),
        (2000, "$20 bill"),
        (1000, "$10 bill"),
        (500, "$5 bill"),
        (100, "$1 bill"),
        (25, "quarter"),
        (10, "dime"),
        (5, "nickel"),
        (1, "penny"),
    ]

    change_in_dollars = round(total_change / 100, 2)
    print("Total change: $", change_in_dollars, sep="")

    # Determines how many of each denomination fit into the remaining change.
    for denomination_value, denomination_name in denominations:
        quantity = remaining_change // denomination_value

        if quantity > 0:
            print(f"{denomination_name}: {quantity}")
            remaining_change %= denomination_value

    if total_change == 0:
        print("No bills or coins are required.")


make_change()
