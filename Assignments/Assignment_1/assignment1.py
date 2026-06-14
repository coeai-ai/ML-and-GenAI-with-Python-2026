# 1. Find area of Rectangle 
length = 4
breadth = 5
area = length * breadth 
print("Area of Rectangle with length",length,"and breadth ",breadth,"is:",area)
print('')
print('')
# 2. Find Simple Interest
p= 4000
r=2.5
t= 5
si=(p*r*t)/100
print("Simple Interest is :",si)
print('')
print('')
#3. Convert temperature from Celsius to Fahrenheit
temp = 100
f = 9*temp/5+32
print("temperature in fahrenheit is :",f) 
print('')
print('')
#4. Calculate Average of three numbers
a=6
b=12
c=18
avg = (a+b+c)/3
print("average of numbers",a,',',b,'and',c,'is:',avg)
print('')
print('')
#5. Find square and cube of a number
num = 6
square = num**2
cube = num**3
print('Square and cube  of number',num,'is:',square ,'and',cube,'respectively')
print('')
print('')
# 6. Swap two numbers without  third variable
num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
print("number before swapping is :",num1,'and',num2)
num1,num2 = num2,num1
print("number after swapping is :",num1,'and',num2)
print('')
print('')
#7. Create a Student Report Program that take student details using input() ,Store marks in variables , Calculate total and percentage , Use Comments ,Use proper indentation
name = input("Enter name of stduent:")
print("Enter marks out of 100 for all subjects")
e=float(input("Enter english marks :"))
m=float(input("Enter mathematics marks :"))
h=float(input("Enter hindi marks :"))
s=float(input("Enter science marks :"))
ss=float(input("Enter socialscience marks :"))
total = e+m+h+s+ss
percentage = total/5
print('Student',name,'has got a total of',total,'marks out of 500','and ','has a percentage :',percentage)

