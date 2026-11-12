# Nye Wade
# CYBR108 Programming Essentials Cyber
# Midterm: R-1.6

""" R-1.6 Sum of Odd Squares
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
"""
"""
To test this function, I used a few values of n, including small boundary
cases like 1 and 2, and an odd n to make sure n itself isn't included.
"""


def sum_odd_squares(n):
    # Created a running total that starts at 0.
    total = 0

    # Iterates through every odd positive integer smaller than n.
    # Starting at 1 and stepping by 2 skips the even numbers, and the stop
    # value n is never included.
    for number in range(1, n, 2):
        total += number * number

    return total


print(sum_odd_squares(1))   # 0, no odd positives smaller than 1
print(sum_odd_squares(2))   # 1
print(sum_odd_squares(6))   # 1 + 9 + 25 = 35
print(sum_odd_squares(7))   # 7 isn't smaller than 7, so still 35
print(sum_odd_squares(10))  # 1 + 9 + 25 + 49 + 81 = 165
