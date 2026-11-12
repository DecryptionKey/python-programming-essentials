""" Second Largest
    Given a list of positive integers, return the distinct second largest
    element. Return -1 when a distinct second largest value does not exist.
"""


def getSecondLargest(arr):
    # Created a set to remove duplicate values from the given list (arr).
    distinct_values = set(arr)

    # Checks that at least two distinct values exist before accessing the second largest.
    if len(distinct_values) >= 2:
        # Returns the second value from the end after sorting the distinct values.
        return sorted(distinct_values)[-2]

    # Returns -1 when a distinct second largest value does not exist.
    return -1


# Prints the results returned by the function for each test case.
print(getSecondLargest([12, 35, 1, 10, 34, 1]))
print(getSecondLargest([10, 5, 10]))
print(getSecondLargest([80, 80, 80]))
print(getSecondLargest([2, 1]))
