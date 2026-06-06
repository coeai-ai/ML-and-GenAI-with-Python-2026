name = str(input("Enter student name: "))
roll_no = int(input("Enter roll number: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
total = maths + science + english
percentage = total / 3
print("Student Report")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)