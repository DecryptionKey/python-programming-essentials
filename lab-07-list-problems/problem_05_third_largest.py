""" Third Largest
    Given a list of positive integers, return the third largest element. Return
    -1 when the list contains fewer than three elements.
"""


def thirdLargest(arr):
    # Checks that the given list (arr) contains at least three values.
    if len(arr) >= 3:
        # Returns the third value from the end of a sorted copy, including duplicates.
        return sorted(arr)[-3]

    # Returns -1 when there are not enough values to determine the third largest.
    return -1


# Prints the result returned by the function.
print(thirdLargest([13, 16, 57, 85]))
