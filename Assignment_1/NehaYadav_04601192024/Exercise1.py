print("Area of rectangle")
side_1 = int(input("Enter 1st side: "))
side_2 = int(input("Enter 2nd side: "))
print("the area of the rectangle is:", side_1*side_2)

print("Simple Interest")
p = int(input("Enter the Principal: "))
r = int(input("enter the rate: "))
t = int(input("Enter the time: "))
print("Simple Interest is", (p*r*t)/100)

print("From celsius to Farenheit")
c = int(input("Enter the temp in celsius: "))
print("the temp in Farenheit:", ((9/5)*c)+32)

print("Avg of 3 numbers")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print("The avg of the 3 numbers is", (a+b+c)/3)

print("sqr and cube of a number")
num = int(input("Enter the number: "))
print("Square of the number is:", num*num)
print("Cube of the number is:", num*num*num)

print("swapping without 3rd variable")
a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a1,a2 = a2,a1
print("a1 =", a1, "a2 =", a2)

print("Student Report")
# taking student data
eng = int(input("Enter marks of english: "))
hin = int(input("Enter marks of hindi: "))
maths = int(input("Enter marks of maths: "))
#calculating total and percentage
total = eng+hin+maths
percen = (total/300)*100
#printing total and percentage