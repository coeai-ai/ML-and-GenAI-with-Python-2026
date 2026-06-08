# 1. Find area of rectangle. 
side1 = int(input("enter first side: ")) #input first side from user
side2 = int(input("enter second side: ")) #input second side from user
print("area of rectangle: ",side1*side2)

# 2. Find simple interest. 
p_amount = int(input("enter principal amount: ")) #taking user input
rate = int(input("enter the rate: ")) #taking user input
time = int(input("enter the time: ")) #taking user input
print("simple interest: ",(p_amount*rate*time)/100)

# 3. Convert temperature from Celsius to Fahrenheit. 
temp_celsius = int(input("enter temperature in degree celsius: ")) #taking user input
temp_fahrenheit = (9/5*temp_celsius)+32
print("temperature in fahrenheit: ",temp_fahrenheit)

# 4. Calculate average of 3 numbers. 
num1 = int(input("enter first number: ")) #taking user input
num2 = int(input("enter second number: ")) #taking user input
num3 = int(input("enter third number: ")) #taking user input
print("average: ",(num1+num2+num3)/3)

# 5. Find square and cube of a number. 
num =  int(input("enter the number: "))
print("square of number: ",num*num)  #calculating square
print("cube of number: ",num*num*num) #calculating cube

# 6. Swap two numbers without third variable.
a = 5
b = 10

a = a + b  # a = 15
b = a - b  # b = 5
a = a - b  # a = 10
print(a)
print(b)

# 7. Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage 
phy_marks = int(input("enter physics marks: "))
chem_marks = int(input("enter chemistry marks: "))
maths_marks = int(input("enter maths marks: "))
print("total marks: ",phy_marks+chem_marks+maths_marks)
print("percentage of marks: ",((phy_marks+chem_marks+maths_marks)/3)*100)



