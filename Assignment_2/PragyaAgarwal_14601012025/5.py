# Student Result System

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total = 0

# Input marks of 5 subjects
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

# Calculate percentage
percentage = total / 5

# Display grade
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

# Display Result
print("\nStudent Result")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)