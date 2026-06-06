# Student Result System
print("---------- Student Details ----------")
name = input("Enter Student Name: ")
rno = input("Enter Roll Number: ")
print("\n")

print("---------- Marks ----------")
m1 = float(input("Marks obtained in Mathematics(out of 100): "))
m2 = float(input("Marks obtained in Physics(out of 100): "))
m3 = float(input("Marks obtained in Chemistry(out of 100): "))
print("\n")

t_marks = m1 + m2 + m3
per = (t_marks/300) * 100

print("\n-----------------------------------------")
print("           STUDENT REPORT CARD           ")
print("-----------------------------------------")

print("\nStudent Name: ", name)
print("Roll Number : ", rno)

print("\n------- Subject Report -------")

print("Mathematics : ", m1)
print("Physics     : ", m2)
print("Chemistry   : ", m3)

print("\n------- Result -------")

print("Total Marks : ", t_marks)
print("Percentage  : ", per, "%") 
print("Grade       : ", end = "")
if per >= 93:
    print(" A+")
elif per >= 85:
    print(" A")
elif per >= 77:
    print(" B+")
elif per >= 69:
    print(" B")
elif per >= 61:
    print(" C+")
elif per >= 53:
    print(" C")
elif per >= 45:
    print(" D")
else:
    print(" F")