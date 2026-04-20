# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\n--- Result ---")

# Using if-else to compare two numbers
if num1 > num2:
    print(num1, "is greater than", num2)
    print(num2, "is smaller than", num1)

elif num1 < num2:
    print(num2, "is greater than", num1)
    print(num1, "is smaller than", num2)

else:
    print("Both numbers are equal:", num1, "=", num2)