# Input student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

total_marks_obtained = 0

print("--- Enter Marks for 5 Subjects (Out of 100) ---")
for i in range(1, 6):  
    marks = float(input("Enter marks: "))
    total_marks_obtained += marks 

# Calculate percentage based on 500 maximum possible marks
max_possible_marks = 500
percentage = (total_marks_obtained / max_possible_marks) * 100

# Display grade based on percentage
if percentage >= 90:
    grade = "Grade A"
elif percentage >= 75:
    grade = "Grade B"
else:
    grade = "Grade C"

# Display student details and results
print("Name: ", student_name)
print("Roll Number: ", roll_number)
print("Percentage: ", percentage)
print("Final Grade: ", grade)
