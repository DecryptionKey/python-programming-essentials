""" 10. Handle AttributeError Exception in List Operations
        Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
"""
"""
This function is tested by the append statements for the "courses" and
"credit_hours" lists. CYBR108 appends successfully because I used the existing
list method ".append". However, the credit hour number "3" is not added to the
"credit_hours" list because ".appendx" does not exist, producing AttributeError.
"""


def attribute_error():
    # Implemented a try block to monitor the .append operation for a possible exception.
    try:
        # Created an empty list called courses to hold course names.
        courses = []
        # Append statement to add the course "CYBR108" to the courses list.
        courses.append("CYBR108")
        print(courses)

        # Created another empty list called credit_hours to hold the course's credit hour number.
        credit_hours = []
        # Append statement to add the credit hours for "CYBR108" to the list.
        credit_hours.appendx(3)
        print(credit_hours)

    # Handles AttributeError if the list method does not exist.
    except AttributeError as ae:
        print("The method you're attempting to utilize does not exist. Please try again.")
        print(ae)


attribute_error()
