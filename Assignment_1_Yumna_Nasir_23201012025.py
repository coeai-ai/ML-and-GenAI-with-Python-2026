#ASSIGNMENT 1

#1. Find area of rectangle.
x = int(input("Enter length of rectangle:"))
y = int(input("Enter breadth of rectangle:"))
res = x * y
print("Area of rectangle is",res)

#2. Find simple interest.
def fun(p, t, r):
    return (p * t * r) / 100
p = int(input("Enter principal amount:"))
t = int(input("Enter time period:"))
r = int(input("Enter rate of interest:"))
res = fun(p, t, r)
print("Simple interest is", res)

#3. Convert temperature from Celsius to Fahrenheit. 
c = float(input("Enter temperature in celsius: "))
f = (c * 1.8) + 32
print("Temperature in Celsius", str(c))
print("Temperature in Fahrenheit", str(f))

#4. Calculate average of 3 numbers. 
num1 = int(input("Enter value 1:"))
num2 = int(input("Enter value 2:"))
num3 = int(input("Enter value 3:"))
sum_numbers = num1 + num2 + num3
average = sum_numbers / 3
print(f'Sum of 3 numbers: {sum_numbers}, Average of 3 numbers: {average}')

#5. Find square and cube of a number. 
n = int(input("Enter the value: "))
square = n ** 2
cube = n ** 3
print("Square of the number :", square)
print("Cube of the number :", cube)

#6. Swap two numbers without third variable.
x, y = 5, 7
print("Before swapping:", x, y)
x, y = y, x
print("After swapping:", x, y)

#7. Create a Student Report Program that take student details using input(), store marks in variables, calculate total and percentage , use comments, use proper indentation
name = input("Enter student's name: ")
roll_no = input("Enter student's roll number: ")
student_class = input("Enter student's class: ")
division = input("Enter student's division: ")
print("\nEnter marks for the following subjects (out of 100):")
maths_marks = float(input("Maths: "))
english_marks = float(input("English: "))
science_marks = float(input("Science: "))
social_science_marks = float(input("Social Science: "))
it_marks = float(input("IT: "))
total_marks = maths_marks + english_marks + science_marks + social_science_marks + it_marks
number_of_subjects = 5
average_marks = total_marks / number_of_subjects
percentage=total_marks/500*100
print("\n--- Student Report ---")
print(f"Name: {name}")
print(f"Roll Number: {roll_no}")
print(f"Class: {student_class}")
print(f"Division: {division}")
print(f"Total Marks: {total_marks:.2f}") 
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}")


