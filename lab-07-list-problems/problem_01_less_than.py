"""
Less Than
    Given a number k and a list arr that contains integers, return a list of
    numbers that are less than k.
"""


def lessThan(arr, k):
    # Created a separate list to hold values less than k without changing arr.
    results = []

    # Iterates through each value in the given list (arr).
    for number in arr:
        # Adds the current value when it is strictly less than k (the given number).
        if number < k:
            results.append(number)

    # Returns the collected values after every number has been checked.
    return results


# Prints the results returned by the function.
print(lessThan([1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 23, 24, 4634654, 628468], 8))

