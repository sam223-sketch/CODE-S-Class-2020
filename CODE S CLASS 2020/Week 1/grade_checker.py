'''Write a simple grading system that does the following.

    Ask the user for their mark between 0 and 100.
    Prints out the grade for the mark from A - F.
    Use the following rules to determine the grade.

    Greater than 85 is A.
    Between 75 and 85 is B.
    Between 65  and 75 is C.
    Between 55 and 65 is D.
    Between 45 and 55 is E.
    Anything below 45 is F.'''

grade = float(input("Enter your mark here to know your grade:\n"))

if grade >= 86:
    print("Grade is A")
elif grade >= 76:
    print("Grade is B")
elif grade >= 66:
    print("Grade is C")
elif grade >= 56:
    print("Grade is D")
elif grade >= 45:
    print("Grade is E")
else:
    print("Grade is F")