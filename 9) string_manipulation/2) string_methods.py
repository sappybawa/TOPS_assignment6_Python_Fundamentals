# Program to demonstrate string manipulation using various string methods

text = "  Hello Python World  "

# Strip whitespace
print("Stripped string:", text.strip())

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Replace substring
print("Replace 'Python' with 'Programming':", text.replace("Python", "Programming"))

# Split into words
print("Split into words:", text.split())

# Find position of a substring
print("Index of 'World':", text.find("World"))

# Count occurrences of a character
print("Count of 'o':", text.count("o"))

# Join characters with a separator
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("Joined with '-':", "-".join(chars))
