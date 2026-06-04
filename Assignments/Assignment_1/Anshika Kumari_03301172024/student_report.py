# Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of three subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = total / 3

# Displaying report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
