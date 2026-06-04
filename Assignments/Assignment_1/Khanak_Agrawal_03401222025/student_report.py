# Student Report Program

# Student details
name = input("Enter Student Name: ")
rno = input("Enter Roll Number: ")

# Marks of three subjects
a = float(input("Enter marks in Subject 1: "))
b = float(input("Enter marks in Subject 2: "))
c = float(input("Enter marks in Subject 3: "))

# Total marks obtained
total = a + b + c

# Percentage calculation
per = total / 3

# Student Report
print("\n-------- STUDENT REPORT --------\n")
print("Name: ", name)
print("Roll Number: ", rno)
print("Total Marks: ", total)
print("Percentage: ", per, "%")
print("\n--------------------------------\n")