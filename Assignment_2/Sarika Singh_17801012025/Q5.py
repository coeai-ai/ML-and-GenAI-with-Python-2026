name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)