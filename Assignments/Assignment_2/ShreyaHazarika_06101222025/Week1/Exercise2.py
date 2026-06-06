# Taking an integer input from the user
num = int(input("Enter a number to find its factorial: "))

factorial = 1
count = num

# Loop until count reaches 1
while count > 0:
    factorial *= count  # Multiplication assignment operator
    count -= 1          # Decrement count

print("The factorial of", num, "is:", factorial)
