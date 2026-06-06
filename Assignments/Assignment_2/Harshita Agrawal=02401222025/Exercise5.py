# Program to generate a report card for a student

print("Enter Student Details ")
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

print("Enter Marks (out of 100) ")

# Taking marks for three subjects as input from the user
math_marks = float(input("Mathematics marks: "))
physics_marks = float(input("Physics marks: "))
coding_marks = float(input("Computer Science marks: "))

# Calculating total marks and percentage
total_marks = math_marks + physics_marks + coding_marks
max_marks = 300
percentage = (total_marks / max_marks) * 100

# Printing the formatted report card

print("\n          STUDENT REPORT CARD         ")

print(" Student Name : ",student_name)
print(" Roll Number  : ",roll_number)

print("\n Subject Scores")

print(" Mathematics : ",math_marks)
print(" Physics     : ",physics_marks)
print(" Coding      : ",coding_marks)

print("\n Grade Summary")

print(" Total Marks : ",total_marks)
print(" Percentage  : ",percentage) 
print(" Grade       : ",end="")
if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >= 60:
    print("D")
else:
    print("F")