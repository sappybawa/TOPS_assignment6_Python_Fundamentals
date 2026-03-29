"""
PEP 8 Demonstration Program
This script shows correct use of indentation, comments, and variables.
"""

# Define a constant (written in ALL_CAPS as per PEP 8)
PI = 3.14159


def calculate_area_of_circle(radius):
    """Return the area of a circle given its radius."""
    # Formula: Area = π * r^2
    area = PI * (radius ** 2)
    return area


def main():
    """Main function to demonstrate PEP 8 style."""
    # Variable names are lowercase_with_underscores
    circle_radius = 5

    # Call the function and store result
    circle_area = calculate_area_of_circle(circle_radius)

    # Print result with clear formatting
    print(f"The area of a circle with radius {circle_radius} is {circle_area:.2f}")

# Standard Python convention: run main() only if executed directly
if __name__ == "__main__":
    main()