""" 👉 Write a Python program that:

Defines a function grade(marks) that returns the grade (A+, A, B, C, D, F).

Calls the function with different marks (like 95, 72, 40, 20).

Prints the returned grade for each.
"""
# CODE BEGINS HERE ==>

def grade(marks):
    if grade(marks) == 100:
        return "CONGRATULATIONS!!! YOU GOT AN A+."
    elif grade(marks) < 100 and grade(marks) >= 90:
        return "CONGRATUALATIONS YOU GOT AN A.":
    elif grade(marks) < 90 and grade(marks) >= 70:
        return "You got a B."
    elif grade(marks) < 70 and grade(marks) >= 50:
        return "You got a C.":
    elif grade(marks) < 50 and grade(marks) >= 33:
        return "You got a D."
    elif grade(marks) < 33:
        return "You got a F."
    else:
        return "The entered number is not valid."
grade(marks)
    