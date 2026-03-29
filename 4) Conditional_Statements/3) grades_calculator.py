"""
Program: Grade Calculator
Demonstrates how to use if-else ladder to assign grades based on percentage.
"""

# Input percentage
percentage = float(input("Enter your percentage: "))

# If-else ladder for grade calculation
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
