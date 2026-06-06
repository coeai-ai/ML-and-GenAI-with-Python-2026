# Student Result System

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks
total_marks = 0
subjects = 5

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total_marks += marks

# Calculate percentage
percentage = total_marks / subjects

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

# Display result
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)