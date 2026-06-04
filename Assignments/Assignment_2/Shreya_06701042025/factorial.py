# Program to find factorial of a number

# Input from user
num = int(input("Enter a number: "))

# Initialize factorial
fact = 1

# Calculate factorial
for i in range(1, num + 1):
    fact = fact * i

# Display result
print("Factorial of", num, "=", fact)