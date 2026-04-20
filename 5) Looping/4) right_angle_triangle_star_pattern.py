"""Practical Example 4: Print this pattern using nested for loop: """

number = 6

for i in range(1,number):
    for j in range(i):
        print("*", end=" ")
    print()