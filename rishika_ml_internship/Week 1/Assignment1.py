#Find area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is: ", area)

#Find simple interest
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest(in % per annum): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal_amount * rate_of_interest * time) / 100
print("The simple interest is: ", simple_interest)

#Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = ((celsius * 9)/5) + 32
print("The temperature in Fahrenheit is: ", fahrenheit)

#Calculate average of 3 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is: ", average)

#Find square and cube of a number
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("The square of the number is: ", square)
print("The cube of the number is: ", cube)

#Swap two numbers without using third variable
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("The first number is: ", num1)
print("The second number is: ", num2)

# Create a Student Report Program that takes student details, inputs dynamic subjects, stores marks, and calculates total/percentage
student_name = input("Enter the student name: ")
student_rollno = int(input("Enter the student roll number: "))
student_grade = input("Enter the student grade: ")

# Input the number of subjects
num_of_subjects = int(input("Enter the number of subjects: "))

# Store marks in a list (variables)
subject_marks = []
for i in range(num_of_subjects):
    marks = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
    subject_marks.append(marks) #.append() is a method which is used to add elements to the end of a list

# Calculate total and percentage
total_marks = sum(subject_marks) # sum() is a function which is used to calculate the sum of all the elements in a list
percentage = (total_marks / num_of_subjects)

print("\nStudent Report Card")
print("Name: ", student_name)
print("Roll Number: ", student_rollno)
print("Grade: ", student_grade)
print("Total Marks: ", total_marks)
print("Percentage: ", percentage, "%")
