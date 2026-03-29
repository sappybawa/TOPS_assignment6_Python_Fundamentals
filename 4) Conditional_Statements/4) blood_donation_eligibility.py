"""
Program: Blood Donation Eligibility Checker
Demonstrates nested if-else conditions in Python.
"""

# Input details
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))

# Outer condition: check age
if age >= 18:
    # Inner condition: check weight
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood (weight must be at least 50 kg).")
else:
    print("You are not eligible to donate blood (age must be at least 18).")
