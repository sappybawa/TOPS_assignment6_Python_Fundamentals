"""
Program: Demonstrating Variables and Data Types in Python
"""

# Integer
age = 19
print("Age:", age, "Type:", type(age))

# Float
height = 5.9
print("Height:", height, "Type:", type(height))

# String
name = "Sappy"
print("Name:", name, "Type:", type(name))

# --- Boolean ---
is_student = True
print("Is Student:", is_student, "Type:", type(is_student))

# List (ordered, mutable)
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits, "Type:", type(fruits))

# Tuple (ordered, immutable)
coordinates = (10, 20)
print("Coordinates:", coordinates, "Type:", type(coordinates))

# Dictionary (key-value pairs)
student = {"name": "Sappy", "age": 19, "course": "Python"}
print("Student:", student, "Type:", type(student))

# Set (unordered, unique elements)
unique_numbers = {1, 2, 3, 3}
print("Unique Numbers:", unique_numbers, "Type:", type(unique_numbers))
