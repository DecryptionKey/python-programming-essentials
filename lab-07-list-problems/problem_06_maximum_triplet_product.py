""" Maximum Triplet Product
    Given a list, return the maximum product that can be obtained by multiplying
    any three elements of the list.
"""


def maxTripletProduct(arr: list[int]) -> int:
    # Created a sorted copy so the smallest and largest values are easy to access.
    sorted_values = sorted(arr)

    # Multiplies the three largest values to create the first possible maximum.
    largest_product = (sorted_values[-1] * sorted_values[-2] * sorted_values[-3])

    # Two negative values can produce a larger positive product with the largest value.
    smallest_product = sorted_values[0] * sorted_values[1] * sorted_values[-1]

    # Returns whichever candidate has the greater product.
    if largest_product > smallest_product:
        return largest_product
    return smallest_product

# Prints the results returned by the function for each test case.
print(maxTripletProduct([-10, -8, 1, 2, 5]))        # Expected: 400
