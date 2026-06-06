# This program takes student details and subject marks,
# then calculates the total score and final percentage.

print("--- Enter Student Details ---")
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

print("--- Enter Marks (out of 100) ---")
# Storing individual subject marks into distinct float variables
math_marks = float(input("Mathematics marks: "))
physics_marks = float(input("Physics marks: "))
coding_marks = float(input("Computer Science marks: "))

# Calculating cumulative total and percentage score
total_marks = math_marks + physics_marks + coding_marks
max_marks = 300
percentage = (total_marks / max_marks) * 100

# Printing a well-structured, formatted student report card
print("=====================================")
print("           STUDENT REPORT            ")
print("=====================================")
print("Name        :", student_name)
print("Roll No     :", roll_number)
print("-------------------------------------")
print("Mathematics :", math_marks)
print("Physics     :", physics_marks)
print("Coding      :", coding_marks)
print("-------------------------------------")
print("Total Marks :", total_marks, "/", max_marks)
print("Percentage  :", percentage, "%")
print("=====================================")
