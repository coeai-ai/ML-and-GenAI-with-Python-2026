#ques 1 : function to  print first 10 natural numbers.
def numbers():
    for i in range(1, 11):
        print(i)
numbers()

#ques 2 : function to calculate sum of first N natural numbers.
def sumOfNumbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    print("The sum of", n , "natural numbers is:", sum)
nterms = int(input("Enter the natural numbers u need sum of: "))
sumOfNumbers(nterms)

#ques 3 : function to reverse a number.
def reverse_no(num):
    reverse = 0 
    while num >0:
        n = num % 10
        reverse = (reverse * 10) + n
        num = num // 10
    print("The reversed number is:", reverse)
num = int(input("Enter the number: "))
reverse_no(num)

#ques 4 : function to count digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        num % 10
        count += 1
        num = num // 10
    print("The digits in the number are:", count)
num = int(input("Enter the number: "))
count_digits(num)

#ques 5 : function to check palindrome number.
def isPalindrome(num):
    reverse = 0 
    a = num
    while num >0:
        n = num % 10
        reverse = (reverse * 10) + n
        num = num // 10
    if reverse == a:
        print("The number is a palindrome")
    else:
        print("The number is Not  palindrome")
num = int(input("Enter a number: "))
isPalindrome(num)

#ques 6 : function to generate Fibonacci series.
def fibonacci(num):
    a , b = 0 , 1
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)
num = int(input("Enter a number of terms for fibonacci series: "))
fibonacci(num)

#ques 7 : Calculator Using Functions that contains the following features;
#-	User selects operation 
#	-	Program performs calculation 
#	-	Display result
def add(x, y):
    print("The sum is:", x + y)

def subtract(x, y):
    print("The difference is:", x - y)

def multiply(x, y):
    print("The product is:", x * y)

def divide(x, y):
    if y == 0:
        return "ERROR: Division by 0 is not possible..."
    print("The quotient is:", x / y) 

def Calculator():
    print("--- Calculator---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = (input("Enter the choice [1-4]: "))
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            return
        
        if choice == '1':
            add(num1, num2)
        elif choice == '2':
            subtract(num1, num2)
        elif choice == '3':
            multiply(num1, num2)
        elif choice == '4':
            divide(num1, num2)
        else:
            print("Invalid operation selected....try again")
        
if __name__ == "__main__":
    Calculator()

#ques 8 : Create a text file and store student details.
def save_student_details(filename="student_details.txt"):
    students = [
        {"id": "S1001", "name": "Annie", "major": "Computer Science", "gpa": "3.8"},
        {"id": "S1002", "name": "Reiner", "major": "Data Science", "gpa": "3.5"},
        {"id": "S1003", "name": "Berthold", "major": "Mathematics", "gpa": "3.9"}
    ]
    try:
        with open(filename, "w") as file:
            file.write("--- Student Directory ---\n")
            for student in students:
                record = f"ID: {student['id']} | Name: {student['name']} | Major: {student['major']} | GPA: {student['gpa']}\n"
                file.write(record)
        print(f"Success: Details written to '{filename}' successfully.")
    except IOError as e:
        print(f"Error: Could not write to file. {e}")
if __name__ == "__main__":
    save_student_details()

#ques 9 : Read data from a file. 
try:
    with open("student_details.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The specified file does not exist.")

#ques 10 : Handle division by zero using exception handling
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"Calculation successful. Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please check your inputs.")
num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
safe_divide(num1, num2)

#ques 11 : Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)
    def display_details(self):
        print(f"--- Student Profile: {self.name} ---")
        print(f"Scores: {self.marks}")
        print(f"Average Mark: {self.get_average():.2f}")
        print("-" * 30)
if __name__ == "__main__":
    student1 = Student("Alice Smith", [85, 92, 78, 90])
    student2 = Student("Bob Jones", [70, 65, 82, 74])
    student1.display_details()
    student2.display_details()