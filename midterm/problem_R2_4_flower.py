# Nye Wade
# CYBR108 Programming Essentials Cyber
# Midterm: R-2.4

""" R-2.4 Flower Class
    Write a Python class, Flower, that has three instance variables of type
    str, int, and float, that respectively represent the name of the flower,
    its number of petals, and its price. Your class must include a constructor
    method that initializes each variable to an appropriate value, and your
    class should include methods for setting the value of each type, and
    retrieving the value of each type.
"""
"""
To test this class, I created a Flower, printed each value with the getters,
changed each value with the setters, and printed them again to confirm the
updates stuck.
"""


class Flower:
    """A flower with a name, a number of petals, and a price."""

    def __init__(self, name, petals, price):
        # Initializes each instance variable, converting to the required type.
        self._name = str(name)
        self._petals = int(petals)
        self._price = float(price)

    # Getters return the current value of each instance variable.
    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    # Setters update each instance variable, keeping the required type.
    def set_name(self, name):
        self._name = str(name)

    def set_petals(self, petals):
        self._petals = int(petals)

    def set_price(self, price):
        self._price = float(price)


rose = Flower("Rose", 32, 2.50)
print(rose.get_name(), rose.get_petals(), rose.get_price())

rose.set_name("Tulip")
rose.set_petals(6)
rose.set_price(1.75)
print(rose.get_name(), rose.get_petals(), rose.get_price())
