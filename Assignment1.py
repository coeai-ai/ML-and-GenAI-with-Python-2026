#Assignment 1

#a Area of rectangle
length=5
breadth=4
Area=length*breadth
print(Area)

#b Simple Interest
principle=1000
rate=2
time=5
simple_interest=(principle*rate*time)/100
print(simple_interest)

#c Celsius to Farenheit
temp_celsius=35
temp_farenheit=(1.8*temp_celsius)+32
print(temp_farenheit)

#d Average of 3 numbers
num1,num2,num3=10,20,30
average=(num1+num2+num3)/3
print(average)

#e Square and Cube
num=2
square=num**2
cube=num**3
print(square)
print(cube)

#f Swapping two numbers
x,y=10,20
print("Before swapping:","x=",x,"y=",y)
x,y=y,x
print("After swapping:","x=",x,"y=",y)

#g Student Report
student_name=input("Enter Student's Name:") # taking student's name as input from the user

#taking input of marks of the student for 5 subjects-
#typecasting to convert input into integer values
sub1=int(input("Enter marks of subject1:")) 
sub2=int(input("Enter marks of subject2:")) 
sub3=int(input("Enter marks of subject3:"))
sub4=int(input("Enter marks of subject4:"))
sub5=int(input("Enter marks of subject5:"))

total_marks=sub1+sub2+sub3+sub4+sub5 # calculating total marks out of 500
percentage=(total_marks/500)*100 #calculating percentage

# printing the result of the student
print(student_name,"your result is:","total marks=",total_marks,"percentage=",percentage)