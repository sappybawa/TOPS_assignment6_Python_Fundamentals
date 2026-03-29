# Taking input from user
number = int(input("Enter a number: "))
count = 0

# Check Prime or not
for i in range(1, number):
    if number % i == 0:
        count+=1

if count > 2:
    print("The number", number, "is not a prime number")
else:
    print("The number", number, "is a prime number")