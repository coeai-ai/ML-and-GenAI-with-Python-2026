# Program to calculate Simple Interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)