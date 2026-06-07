#1) find area of rectangle
a=float(input("enter 1st side="))
b=float(input("enter 2nd side="))
area=a*b
print(area)
#2)find simple interest
p=float(input("enter principle amount="))
r=float(input("enter rate="))
t=float(input("enter time="))
si=p*r*t/100
print(si)
#3)convert temp from celsius to fahrenite
x=float(input("enter temp in celcius="))
f = x* 9/5 + 32
print(f)
#4) avg of 3 numbers
s=int(input("enter 1st number="))
u=int(input("enter 2nd number="))
v=int(input("enter 3rd number="))
avg=s+u+v/3
print(avg)
#5)square and cube of a number
u=int(input("enter the number="))
square=u*u
cube=u*u*u
print(square)
print(cube)
#5)swap two numbers
d=int(input("enter number="))
e=int(input("enter number="))
d,e=e,d
print(d)
print(e)
#6)student report program
student_name=input("enter student name=")
student_age=int(input("enter the age of the student="))
student_class=int(input("enter the class of teh student="))
marks1=float(input("enter the marks of 1st subject="))
marks2=(float(input("enter the marks of 2nd subject=")))
marks3=float(input("enter the marks of 3rd subject="))
total=marks1+marks2+marks3
percentage=total/3
print(student_name)
print(student_age)
print(student_class)
print(marks1)
print(marks2)
print(marks3)
print(total)
print(percentage)