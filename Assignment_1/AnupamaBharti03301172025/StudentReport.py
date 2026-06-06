# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
# Taking marks for subjects
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))
# Calculating total and percentage
total = maths + science + english
percentage = total / 3
# Displaying student report
print()
print("----- Student Report -----")
print("Name of the Student:", name)
print("Roll Number of the Student:", roll_no)
print("Total Marks :", total)
print("Percentage :", percentage, "%")
