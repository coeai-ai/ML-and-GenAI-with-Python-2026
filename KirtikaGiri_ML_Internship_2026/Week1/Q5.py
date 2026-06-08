# Student Result System

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\n--- Entering details for Student {i+1} ---")
    
    student_name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")
    
    math_marks = float(input("Enter marks for Mathematics (out of 100): "))
    science_marks = float(input("Enter marks for Science (out of 100): "))
    english_marks = float(input("Enter marks for English (out of 100): "))

    total_marks = math_marks + science_marks + english_marks
    percentage = (total_marks / 300) * 100
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"
        
    print("\n================ STUDENT RESULT ================")
    print(f"Name         : {student_name}")
    print(f"Roll No      : {roll_number}")
    print(f"Total Marks  : {total_marks:.2f} / 300")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Final Grade  : {grade}")
    print("================================================")
