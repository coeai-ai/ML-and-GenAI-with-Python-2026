# Taking numeric inputs from user using float() type conversion
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time in years: "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying output using the print() statement
print("Simple Interest =", simple_interest)
