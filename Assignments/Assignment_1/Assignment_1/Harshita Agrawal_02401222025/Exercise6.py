# Taking input for two numbers and swapping their values
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

print("Before Swapping: a =", a, "and b =", b)

# Swapping the values of a and b
a, b = b, a

# Displaying the swapped values
print("After Swapping: a =", a, "and b =", b)