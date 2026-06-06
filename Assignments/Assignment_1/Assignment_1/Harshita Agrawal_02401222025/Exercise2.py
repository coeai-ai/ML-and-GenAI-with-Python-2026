# Taking numeric inputs from user and calculating simple interest
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time in years: "))

# Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying output using the print() statement
print("Simple Interest =", simple_interest)