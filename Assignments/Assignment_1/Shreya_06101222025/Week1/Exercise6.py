# Requesting two input numbers from the user
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

print("Before Swapping: a =", a, "and b =", b)

# Swapping without using a temporary third variable
a, b = b, a

print("After Swapping: a =", a, "and b =", b)
