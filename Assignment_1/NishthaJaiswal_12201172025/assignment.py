#Question 1: Find area of rectangle
length=5
breadth=10
area=length*breadth
print("Area of rectangle is",area)

#Question 2: Find simple interest
principal=1000  #Money borrowed
rate=5          #Interest rate(5%)
time=2          #Time in years
simple_interest=(principal * rate * time) /100
print("Simple Interest is:", simple_interest)

#Question 3: Convert temperature from celsius to farenheit
celsius=37
farenheit=(celsius * 9/5) + 32
print("Temperature in Farenheit is:",farenheit)

#Question 4: Calculate average of 3 numbers
num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3) / 3
print(" Average of the 3 numbers is:", average)

#Question 5: Find square and cube of a number
base_number = 4
square = base_number ** 2
cube = base_number ** 3
print("5. Square is:", square, "and Cube is:", cube)

#Question 6: Swap two numbers without a third variable
a = 5
b = 10
print("6. Before swap: a =", a, ", b =", b)
a, b = b, a  # Magic swap trick!
print("   After swap: a =", a, ", b =", b)

#Question 7: Student Report Program using input()
print("\n---  STUDENT REPORT CARD PROGRAM ---")
# Taking inputs from the keyboard
student_name = input("Enter student name: ")
math_marks = float(input("Enter marks for Math: "))
science_marks = float(input("Enter marks for Science: "))
english_marks = float(input("Enter marks for English: "))
history_marks = float(input("Enter marks for History: "))
coding_marks = float(input("Enter marks for Coding: "))

# Calculating totals
total_marks = math_marks + science_marks + english_marks + history_marks + coding_marks
percentage = (total_marks / 500) * 100

# Displaying the final result
print("\nFinal Result:")
print("Student Name:", student_name)
print("Total Marks Scored:", total_marks, "/ 500")
print("Percentage Scored:", percentage, "%")

