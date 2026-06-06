prin_amt = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

simp_int = (prin_amt * rate * time) / 100

print("Simple Interest =", simp_int)