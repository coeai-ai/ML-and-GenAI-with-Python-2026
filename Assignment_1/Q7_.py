#Que7 Create a Student Report Program
# Student Report Program

# Taking student details using input()
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Taking marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculating total and percentage
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
# Assuming each subject is out of 100, maximum marks = 500
percentage = (total_marks / 500) * 100

# Displaying the report
print("\n--- STUDENT REPORT CARD ---")
print("Name:", student_name)
print("Roll Number:", roll_number)
print("Total Marks Obtained:", total_marks, "/ 500")
print("Percentage:", percentage, "%")