# Program to create a student report

# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of three subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = total / 3

# Displaying student report
print("\n----- Student Report -----")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Subject 1 Marks:", marks1)
print("Subject 2 Marks:", marks2)
print("Subject 3 Marks:", marks3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")