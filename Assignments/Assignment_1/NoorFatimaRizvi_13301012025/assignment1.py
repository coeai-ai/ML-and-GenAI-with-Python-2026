#Area of rectangle
length = 5
breadth = 6
areaOfRectangle = length * breadth
print("The area of rectangle =", areaOfRectangle)

#Simple Interest
p = 1000
r = 5
t = 2
SI = (p*r*t)/100
print("Simple Interest =", SI)

#Celsius to Fahrenheit
celsius = 25
fahrenheit = (9/5 * celsius) + 32
print("Temperature in Fahrenheit =", fahrenheit)

#Average of three numbers
n1 = 8
n2 = 9
n3 = 10
average = (n1+n2+n3)/3
print("The average of numbers =", average)

#Square and cube of a number
n = 3
square = n * n
cube = n * n * n
print("Square =", square)
print("Cube =", cube)

#Swapping numbers
num1 = 10
num2 = 20
num1, num2 = num2, num1
print("After swapping, num1 =", num1, "and num2 =", num2)

#Student Report Program
student_details = {
    "name" : input("Enter your name: "),
    "roll_no" : input("Enter your roll number: ")
}

#Taking input marks from the student
science = int(input("Enter science marks: "))
maths = int(input("Enter maths marks: "))
english = int(input("Enter english marks: "))

# Calculating total and percentage
total = science + maths + english
percentage = (total / 300) * 100

# Displaying report
print("\n----- STUDENT REPORT -----")
print("Name:", student_details["name"])
print("Roll Number:", student_details["roll_no"])
print("Total Marks:", total)
print("Percentage:", percentage, "%")
