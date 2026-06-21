# Generated from: Exercise_5.ipynb
# Converted at: 2026-06-04T14:23:21.507Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = 5
total = 0

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

percentage = total / subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- STUDENT RESULT -----")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)