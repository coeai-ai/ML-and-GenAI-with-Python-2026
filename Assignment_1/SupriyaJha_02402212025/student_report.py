name = input("Name: ")
roll = input("Roll No: ")

dsa = float(input("DSA: "))
ml = float(input("ML: "))
dbms = float(input("DBMS: "))

total = dsa + ml + dbms
percentage = (total / 300) * 100

print("\n--- REPORT ---")
print("Name:", name)
print("Roll:", roll)
print("Total:", total)
print("Percentage:", percentage)
