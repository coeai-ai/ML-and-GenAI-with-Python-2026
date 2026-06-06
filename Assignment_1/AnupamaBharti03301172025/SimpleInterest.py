# Taking principal, rate and time from user
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

# Calculating simple interest
si = (p * r * t) / 100

# Displaying result
print("Simple Interest =", si)
