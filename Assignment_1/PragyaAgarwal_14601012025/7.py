# Student Report Program

# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of 5 subjects
mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
mark4 = float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks
total = mark1 + mark2 + mark3 + mark4 + mark5

# Calculating percentage
percentage = total / 5

# Displaying report
print("\nStudent Report")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")