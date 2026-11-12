# Nye Wade
# CYBR108 Programming Essentials Cyber
# Midterm: R-2.5

""" R-2.5 CreditCard Number Checks
    Use the techniques of Section 1.7 in the textbook to revise the charge and
    make_payment methods of the CreditCard class to ensure that the caller
    sends a number as a parameter.
"""
"""
To test this class, I made valid charges and payments with an int and a float,
then tried passing a string and a boolean and confirmed each one raised a
TypeError that gets caught and printed.
"""


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        Raise TypeError if price isn't a number.
        """
        # Checks that price is an int or float before using it (Section 1.7).
        # bool is a subclass of int, so True and False are rejected separately.
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("price must be numeric")

        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance.

        Raise TypeError if amount isn't a number.
        """
        # Same check as charge so a bad value never touches the balance.
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("amount must be numeric")

        self._balance -= amount


card = CreditCard("Nye Wade", "Example Credit Union", "1234 5678 9012 3456", 1000)

print(card.charge(200))       # True
print(card.charge(50.75))     # True
card.make_payment(100)
print(card.get_balance())     # 150.75

# Tries values that aren't numbers and catches the TypeError.
for bad_value in ["candy", True, None]:
    try:
        card.charge(bad_value)
    except TypeError as error:
        print(f"charge({bad_value!r}) rejected: {error}")

try:
    card.make_payment("fifty")
except TypeError as error:
    print(f"make_payment('fifty') rejected: {error}")

print(card.get_balance())     # still 150.75
