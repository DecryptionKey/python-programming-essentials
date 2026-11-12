""" Segregate Even and Odd Numbers
    Modify a list so all even numbers appear first in sorted order, followed by
    all odd numbers in sorted order.
"""


def segregateEvenOdd(arr):
    # Created separate lists to hold the even and odd values.
    even = []
    odd = []

    # Sorts the given list first so each group is collected in ascending order.
    arr.sort()

    # Iterates through each value in the sorted list (arr).
    for current_num in arr:
        # Collects even values when division by 2 leaves no remainder.
        if current_num % 2 == 0:
            even.append(current_num)
        # Collects the odd values
        else:
            odd.append(current_num)

    # Combines both groups and replaces the values of the original list.
    arr[:] = even + odd

    # Returns the updated list to display the result.
    return arr


# Prints the result returned by the function.
print(segregateEvenOdd([1, 2, 3, 6, 5, 11, 7, 8, 12]))

