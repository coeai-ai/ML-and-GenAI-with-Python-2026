#student record
# student details using input()
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
# marks in variables
math = float(input("Enter marks for Math: "))
science = float(input("Enter marks for Science: "))
english = float(input("Enter marks for English: "))
# Total and Percentage
total_marks = math + science + english
percentage = (total_marks / 300) * 100

# Report
print("\n" + "="*30)
print("       STUDENT REPORT")
print("="*30)
print(f"Name:         {name}")
print(f"Roll Number:  {roll_no}")
print("-" * 30)
print(f"Total Marks:  {total_marks}/300")
print(f"Percentage:   {percentage:.2f}%")
print("="*30)