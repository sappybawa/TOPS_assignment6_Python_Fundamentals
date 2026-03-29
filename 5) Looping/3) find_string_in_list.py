"""Practical Example 3: Write a Python program to find a specific string in the list
 using a simple for loop and if condition"""

fruits_list = ['apple', 'banana', 'mango', 'orange']


fruit_search = input("Enter a fruit to search for: ")

found = False

for fruit in fruits_list:
    if fruit == fruit_search:
        print(fruit_search, "is in the list")
        found = True
        break

if not found:
    print(fruit_search, "The fruit is not in the list")

print()
print("The complete fruit list is: ", fruits_list)