# Program to find the greatest of three numbers
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))

# Comparing the numbers to find the greatest
if x>y and x>z:
    print("The greatest number is:", x)
elif y>x and y>z:
    print("The greatest number is:", y)
else:
    print("The greatest number is:", z)