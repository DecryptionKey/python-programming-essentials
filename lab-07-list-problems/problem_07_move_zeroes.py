""" Move All Zeroes to End
    Move every zero to the end of a list while maintaining the relative order
    of the nonzero values. Modify the original list without an extra list.
"""


def pushZerosToEnd(arr: list[int]) -> list[int]:
    # Created a position variable to track where the next nonzero value belongs.
    position = 0

    # Iterates through every index in the given list (arr).
    for i in range(len(arr)):
        # Copies nonzero values forward, preserving their original order.
        if arr[i] != 0:
            arr[position] = arr[i]
            # Advances the write position only after a nonzero value is copied.
            position += 1

    # Replaces the leftover values with zero, starting after the nonzero values.
    for j in range(position, len(arr)):
        arr[j] = 0

    # Returns the updated original list.
    return arr


# Prints the result returned by the function.
print(pushZerosToEnd([1, 2, 0, 3, 0 , 54, 64, 0, 0, 0, 3, 23, 11, 0, 7]))
