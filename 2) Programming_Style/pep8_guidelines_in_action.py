"""
PEP 8 Demonstration Program
This script shows correct use of indentation, comments, and variables.
"""

# Define a constant (written in ALL_CAPS as per PEP 8)
PI = 3.14159

def calculate_area_of_circle(radius):
    # Formula: Area = π * r^2
    area = PI * (radius ** 2)
    return area

circle_radius = float(input("Enter the radius of the circle: "))

print(calculate_area_of_circle(circle_radius))