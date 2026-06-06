name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
student_class = input("Enter Class/Grade: ")
sub1 = float(input("Enter Marks for Subject 1: "))
sub2 = float(input("Enter Marks for Subject 2: "))
sub3 = float(input("Enter Marks for Subject 3: "))
total_obtained = sub1 + sub2 + sub3
total_possible = 300
percentage = (total_obtained / total_possible) * 100
if percentage >= 90:
        grade = "A"
elif percentage >= 75:
        grade = "B"
elif percentage >= 50:
        grade = "C"
else:
        grade = "Fail"
        
print("\n--- Student Result Sheet ---")
print("Name:", name)
print("Roll Number:", roll_no)
print("Class:", student_class)
print(f"Percentage: {percentage:.2f}%")  
print("Final Grade:", grade)
