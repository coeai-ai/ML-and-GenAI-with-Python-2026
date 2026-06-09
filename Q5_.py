def create_student_result_system():
    print("=== Student Result System ===")
    
    # 1. Input student details
    student_name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    
    # 2. Input marks for subjects
    print("\n--- Enter Marks (out of 100) ---")
    try:
        math = float(input("Mathematics: "))
        science = float(input("Science: "))
        english = float(input("English: "))
    except ValueError:
        print("Invalid input! Please enter numerical values for marks.")
        return

    # Validate that marks are within a realistic range
    if any(m < 0 or m > 100 for m in [math, science, english]):
        print("Error: Marks should be between 0 and 100.")
        return

    # 3. Calculate percentage
    total_marks = math + science + english
    max_marks = 300
    percentage = (total_marks / max_marks) * 100

    # 4. Determine grade based on percentage
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

    # Display the final result
    print("\n================================")
    print("          STUDENT REPORT        ")
    print("================================")
    print(f"Name:        {student_name}")
    print(f"Roll No:     {roll_number}")
    print("--------------------------------")
    print(f"Math:        {math}/100")
    print(f"Science:     {science}/100")
    print(f"English:     {english}/100")
    print("--------------------------------")
    print(f"Total Marks: {total_marks}/{max_marks}")
    print(f"Percentage:  {percentage:.2f}%")
    print(f"Final Grade: {grade}")
    print("================================")

# Run the system
if __name__ == "__main__":
    create_student_result_system()