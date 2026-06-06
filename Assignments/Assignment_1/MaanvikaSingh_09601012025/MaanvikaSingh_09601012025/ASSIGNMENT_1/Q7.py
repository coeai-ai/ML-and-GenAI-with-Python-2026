#Create a Student Report Program that take student
#details using input(), Store marks in variables,
#Calculate total and percentage , Use comments,
#Use proper indentation

#to take student details
name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
grade = input("Enter the student's grade: ")

#to take marks in subjects
math_marks = float(input("Enter the marks in Mathematics: "))
science_marks = float(input("Enter the marks  in Science: "))
english_marks = float(input("Enter the marks in English: "))

#to calculate total marks
total_marks = math_marks + science_marks + english_marks

#to calculate percentage
percentage = (total_marks / 300) * 100

#to display the student report
print("\nStudent Report")
print("Name:", name)
print("Age:", age)
print("Grade:", grade)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")