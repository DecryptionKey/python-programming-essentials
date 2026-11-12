# Nye Wade
# CYBR108 Programming Essentials Cyber
# Midterm: P-1.29

""" P-1.29 All Possible Strings
    Write a Python program that outputs all possible strings formed by using
    the characters c, a, t, d, o, and g exactly once.
"""
"""
To test this function, I used the required characters and confirmed that the program creates 720 unique strings, with every character used exactly once.
"""


def possible_strings(characters):
    # Created a list containing an empty string as the starting point.
    possible_results = [""]

    # Iterates through each required character one at a time.
    for character in characters:
        updated_results = []

        # Inserts the current character into every position of each partial string.
        for partial_string in possible_results:
            for position in range(len(partial_string) + 1):
                new_string = (
                    partial_string[:position]
                    + character
                    + partial_string[position:]
                )
                updated_results.append(new_string)

        possible_results = updated_results

    return possible_results


characters_to_use = "catdog"
results = possible_strings(characters_to_use)

for result in results:
    print(result)

print(f"Total possible strings: {len(results)}")
