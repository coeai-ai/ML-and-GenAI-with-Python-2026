#Find sum of first 10 natural numbers
total_sum = 0
for i in range(1, 11):
    total_sum += i
print("The sum of first 10 natural numbers is: ", total_sum)

#Find factorial of a number.
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("The factorial of the number is: ", factorial)

#Print Fibonacci Series
def fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(f"Fibonacci sequence up to {n} term:")
        print(0)
    else:
        print("Fibonacci sequence:")
        n1, n2 = 0, 1
        count = 0
        while count < n:
            print(n1, end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        print()

n_terms = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci_series(n_terms)
        
#Find largest among 3 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

max_num = max(num1, num2, num3)
print("The largest number is: ", max_num)

#Create Student Result System
#Input student details
student_name = input("Enter the student name: ")
student_rollno = int(input("Enter the student roll number: "))
student_grade = input("Enter the student grade: ")

#Input marks
num_of_subjects = int(input("Enter the number of subjects: "))
subject_marks = []
for i in range(num_of_subjects):
    marks = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
    subject_marks.append(marks)

#Calculate percentage
total_marks = sum(subject_marks)
percentage = (total_marks / num_of_subjects)

#Display grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

#Print result
print("\nStudent Result")
print("Name: ", student_name)
print("Roll Number: ", student_rollno)
print("Grade: ", student_grade)
print("Total Marks: ", total_marks)
print("Percentage: ", percentage, "%")
print("Final Grade: ", grade)
