# Input Student Details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input Marks
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
m4 = float(input("Enter marks in Subject 4: "))
m5 = float(input("Enter marks in Subject 5: "))

# Calculate Total and Percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Grade Calculation
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
print("\n----- STUDENT REPORT -----")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)