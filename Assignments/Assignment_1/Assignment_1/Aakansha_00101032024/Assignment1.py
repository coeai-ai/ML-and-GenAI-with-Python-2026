# 1. To find area of rectangle
l= int(input("Enter lenght of rectangle:"))
w= int(input("Enter width odf rectangle:"))
print("Area of rectangle =", l*w);

# 2.To find simple interest
P= float(input("Enter the principle amount:"))
R= float(input("Enter thw annual interest rate in %:"))
T= float(input("Enter the time period in years:"))
print("Simple Interest = ", (P*R*T)/100);

# 3. Convert temperature from Celsius to Fahrenheit.
C = float(input("Enter temperature in celcius:"))
F = (C*1.8) + 32;
print("Temperture in Fahrenheit is:",F)

# 4. Calculate average of 3 numbers.
a= float(input("Enter first number:"))
b= float(input("Enter second number:"))
c= float(input("Enter third number:"))
Average = (a+b+c)/3;
print("Average of three numbers is:", Average)

# 5. Find square and cube of a number.
num= float(input("Enter a number:"))
print("Square of a number is:", num*num)
print("Cube of a number is:", num*num*num)

# 6. Swap two numbers without third variable.
a= float(input("Enter first number:"))
b= float(input("Enter second number:"))
a = a+b;
b = a-b;
a = a-b;
print("a=",a,"b=",b)

# 7. Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
#Student Details
Student_name=input("Enter student name:")
Student_class=input("Enter class of student:")
Student_roll_no=int(input("Enter roll no. of student"))
print("Enter marks out of 100 for the following subjects:")
#Student marks
Maths=float(input("Mathematics: "))
Science=float(input("Science: "))
English=float(input("English: "))
History=float(input("History: "))
Computer_sci=float(input("Computer Science: "))
Total_marks= Maths + Science + English + History + Computer_sci;
max_possible_marks = 500;
#Calculation of percentage
percentage = (Total_marks / max_possible_marks)*100;
#Student report card
print("Student Report Card ")
print("Student name:", Student_name)
print("Student class:", Student_class)
print("Student roll number:",Student_roll_no) 
print("Marks distribution of each subject out of 100:-")
print("Mathematics: ", Maths)
print("Science: ",Science)
print("English: ",English)
print("History: ",History)
print("Computer Science: ",Computer_sci)
print("Total marks: ",Total_marks)
print("Percentage ",percentage)