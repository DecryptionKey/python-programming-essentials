# Nye Wade
# CYBR108: Programming Essentials Cyber



# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):
    return (n % m) == 0 # I used modulo to check if the number is divisible by m(multiple) w/ no remainder, to determine if it is a multiple.

# Test Cases
# print(is_multiple(8, 4))    # expected t
# print(is_multiple(2, 4))    # expected f
# print(is_multiple(0, 5))    # expected t
# print(is_multiple(-8, 4))   # expected t
# print(is_multiple(7, -3))   # expected f


# R-1.2 Write a short Python function,  is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return (k & 1) == 0 # I used a bitwise operator which is checking the last binary digit for even (0) or odd numbers (1).

# Test Cases
# print(is_even(3)) # expected f
# print(is_even(4)) # expected t
# print(is_even(5)) # expected f
# print(is_even(6)) # expected t


# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min ormax in implementing your solution.

def minmax(data):
    current_min = data[0] # minimum numb
    current_max = data[0] # maximum numb

    for val in data: #iterates through the input (data)
        if val < current_min: #if the current value is less than the stored min, sets the current value as the stored minimum numb
            current_min = val
        elif val > current_max: #mirrored for the maximum number ^
            current_max = val
    return current_min, current_max #returns the min & max as tuple w/ length of 2.
#Test Case
# print(minmax([3,2,68,99,82,34,1,67,12390,7,85090,2026])) # expected 1, 85090

# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    current_sum = 0

    for val in range(1, n):
        current_sum+= (val * val)
    return current_sum

#Test Cases
# print(sum_of_squares(2)) # expected 1
# print(sum_of_squares(3)) # expected 5
# print(sum_of_squares(4)) # expected 14
# print(sum_of_squares(5)) # expected 30
