# Program to create a Student Report

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of three subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# Calculating total marks
total = m1 + m2 + m3

# Calculating percentage
percentage = total / 3

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Marks:", m1, m2, m3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")