# Program to filter out even numbers using filter() and lambda

# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() with a lambda function:
# - lambda x: x % 2 != 0 → returns True if x is odd
# - filter() keeps only elements where the condition is True
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print results
print("Original list:", numbers)
print("Odd numbers (even numbers filtered out):", odd_numbers)
