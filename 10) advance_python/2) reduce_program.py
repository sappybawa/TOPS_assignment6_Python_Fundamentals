# Program to use reduce() to find the product of a list of numbers

from functools import reduce

# Original list
numbers = [1, 2, 3, 4, 5]

# Using reduce() with a function
product = reduce(lambda x, y: x * y, numbers)

# Print result
print("Original list:", numbers)
print("Product of list elements:", product)