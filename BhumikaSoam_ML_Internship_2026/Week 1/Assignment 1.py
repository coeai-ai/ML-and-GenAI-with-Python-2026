#1-area of rectangle

length = int(input("Enter the length of the rectangle : "))
breadth = int(input("Enter the breadth of the rectangle : "))
area = length*breadth
print("area of the rectangle is : ",area)

#2-simple interest
p = int(input("Enter the Principal : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time duration : "))
si = (p*r*t)/100
print("simple interest : ",si)

#3-celsius to fahrenheit
cel = int(input("Enter the temp in degree Celsius : "))
fah = (1.8*cel) + 32
print("in fahrenheit : ",fah)

#4-avg of 3 nums
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))
avg = (num1+num2+num3)/3
print("the average : ",avg)

#5-square and cube
num = int(input("Enter the num : "))
sq = num*num
cube = num**3
print("Square : ",sq, "\t Cube : ",cube)

#6-swap two nums
a = 23
b = 45
print("Original : a = ",a," , b = ",b)
a,b = b,a
print("Swapped : a = ",a," , b = ",b)

#7-Student Report Program
#taking input marks
E = int(input("Enter the marks in English : "))
M = int(input("Enter the marks in Maths : "))
S = int(input("Enter the marks in Science : "))
#calculating total & perc
total = E + M + S
percentage = (total/300)*100
#printing the details
print("scores : Eng = ",E," , Science = ", S, " , Maths = ", M)
print("Total score : ",total)
print("Percentage : ",percentage,"%")
