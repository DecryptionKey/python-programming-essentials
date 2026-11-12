""" 6. Handle IndexError in List Operations
       Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
"""
"""
To test this function input an index outside of the range of the list.
"""

def handle_index():
    # Created a list with some values.
    area_codes = [845, 518, 838, 716]
    # Implemented a try block to monitor the selected list index for a possible IndexError.
    try:
        # Displays the list content to the user.
        print(f"Please select your area code from the list: {area_codes}.")
        print("-------------------------------------------------")
        # Prompts the user to select an index from the list.
        index = int(input("Select an index: "))
        # Checks whether the selected index is below the list's length. Otherwise, the program raises IndexError.
        if index < len(area_codes):
            print(f"The area code you selected is: {area_codes[index]}")
        else:
            raise IndexError
    except IndexError:
        print("Index out of range")


handle_index()
