""" Mean or Average of Array
    Given a list arr, return the floor value of the mean of its elements.
"""

def findMean(arr):
    # Created a running total to hold the sum of the values in arr.
    results = 0

    # Iterates through each value in the given list (arr).
    for number in arr:
        # Adds the current value to the running total.
        results = results + number

    # Floor-divides the completed sum by the item count to round the mean down.
    total = results // len(arr)

    # Returns the floor mean after every number has been added.
    return total


# Prints the result returned by the function.
print(findMean([3, 4, 1, 2, 3, 5, 7, 5, 6, 98, 87, 6, 4, 3, 25, 223, 3, 45, 5, 6, 54, 4]))

