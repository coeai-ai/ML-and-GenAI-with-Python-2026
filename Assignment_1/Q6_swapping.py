#Que6 Swap two numbers without third variable

a = input("Enter first value (a): ")
b = input("Enter second value (b): ")

# Swapping without a third variable
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)