#to Swap two numbers without third variable.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swapping the numbers
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)