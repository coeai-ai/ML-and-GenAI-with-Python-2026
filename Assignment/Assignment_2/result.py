
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = total / 5

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

print("----- STUDENT RESULT -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)