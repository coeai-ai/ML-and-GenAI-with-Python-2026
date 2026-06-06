#Q1.find area of rectangle
#taking length and breadth of rectangle from user
length=float(input("enter the length of rectangle:"))
breadth=float(input("enter the breadth of rectangle:"))
#printing the area
print("the area of rectangle is:" , length*breadth)

#Q2. find simple interest
#taking principle,rate,time from user
p=float(input("enter the principle:"))
r=float(input("enter the rate per annum:"))
t=float(input("enter the time of interest in years:"))
#calculating simple interest
s=(p*r*t)/100
#printing simple interest
print("the simple interest is:",s)

#Q3. celsius to farenheit
#taking the value of temperature in celsius in variable c
c=float(input("enter the temperature in celsius:"))
#converting temperature and storing its value in f
f=(c*1.8) +32
#printing the value of temperature in farenheit
print("the temperature in farenheit is:", f)

#Q4.avg of 3 numbers
#taking 3 numbers from user
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))
#calculating and printing the average of the numbers
print("the average of 3 numbers is:", (num1+num2+num3)/3)

#Q5.square and cube of number
#take the number
num=float(input("enter the number:"))
#calculating and printing the square and cube 
print("the square of", num , "is", num*num)
print("the cube of ", num,"is", num*num*num)

#Q6. swapping numbers
#taking two numbers
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
#swapping
num1,num2=num2,num1
print("after  swapping -first number:",num1,"second number", num2)

#Q7.student report program
#take name and marks os 3 subjects from user
name=input("enter your name:")
sub1=float(input("enter the marks for first subject:"))
sub2=float(input("enter the marks for second subject:"))
sub3=float(input("enter the marks for third subject:"))
#declare max marks and total marks
MAX_MARKS=100
TOTAL_MAX_MARKS=300
#calculating the percentage of each indivisual subject
per_1=(sub1/MAX_MARKS)*100
per_2=(sub2/MAX_MARKS)*100
per_3=(sub3/MAX_MARKS)*100
#printing the output
print("percentage for first subject is:",per_1)
print("percentage for second subject is:",per_2)
print("percentage for third subject is:",per_3)
#calculating and printing the total percentage of marks obtained.
total_per= ((sub1+sub2+sub3)/TOTAL_MAX_MARKS)*100
print("the percentage of total marks obtained by", name,"is",total_per)
