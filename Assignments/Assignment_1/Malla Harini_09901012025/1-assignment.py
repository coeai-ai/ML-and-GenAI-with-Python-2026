#Area of rectangle
length = int(input("Enter length:"))
breadth = int(input("Enter Breadth:"))
print("Area of the rectangle:", length*breadth )

#simple intrest
P= int(input("Enter principal:"))
T = int(input("Enter Time:"))
R = int(input("Enter rate:"))
print("intrest:",P*T*R/100)

#celsius to fahrenheit
C = int(input("Enter Celsius scale:"))
print("In Fahrenheit:", C*1.8 + 32)

#average of 3 numbers
N1 = int(input("Enter 1st num:"))
N2 = int(input("Enter 2nd num:"))
N3 = int(input("Enter 3rd num:"))
average=(N1+N2+N3)/3
print("average:",average)

#sqtuare and cube
N1 = int(input("Enter number to get square and cube:"))
square= N1*N1
cube = square*N1
print("Square=",square, "\nCube=",cube)

#swap 
N1 = int(input("Enter 1st num:"))
N2 = int(input("Enter 2nd num:"))
print("on swapping")
print("2nd number", N1)
print("1st number", N2)
#Method2
print("Before swapping:","1st num=",N1,"2nd num=",N2)
N1,N2=N2,N1
print("After swapping:","1st num=",N1,"2nd num=",N2)

#Student repport program 
total_students=int(input("total number of students:"))

each=int(input("max marks for each subject:"))

for total_students in range(0,total_students):
    Student_name=input("Enter Student name:")
    sub1=int(input("Enter marks of subject 1:"))
    sub2=int(input("Enter marks of subject 2:"))
    sub3=int(input("Enter marks of subject 3:"))
    sub4=int(input("Enter marks of subject 4:"))
    sub5=int(input("Enter marks of subject 5:"))

    print("------Report card of ",Student_name +"------")

    Total= sub1+sub2+sub3+sub4+sub5
    Percentage= (Total*100)/(each*5)

    print("Total marks:",Total)
    print(f"Percentage: {Percentage:.2f}%\n")

print(" submitted by Harini ")
print(" 09901012025 ")
print(" IGDTUW")