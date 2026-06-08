
name = input("Enter student name; ")
roll_no = input("Enter roll number; ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
evs=float(input("Enter English marks: "))


total_marks = maths + science + english + evs


percentage = total_marks  / 4

print("----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)

print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Evs:", evs)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")