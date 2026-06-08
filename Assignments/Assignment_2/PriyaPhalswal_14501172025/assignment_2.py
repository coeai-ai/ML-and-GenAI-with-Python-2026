print("===== ASSIGNMENT 2 =====")
print("1. Sum of First 10 Natural Numbers")
print("2. Factorial of a Number")
print("3. Fibonacci Series")
print("4. Largest Among 3 Numbers")
print("5. Student Result System")

choice = int(input("Enter your choice (1-5): "))

# Q1
if choice == 1:
    total = 0

    for i in range(1, 11):
        total += i

    print("Sum of first 10 natural numbers =", total)

# Q2
elif choice == 2:
    num = int(input("Enter a number: "))

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print("Factorial =", fact)

# Q3
elif choice == 3:
    n = int(input("Enter number of terms: "))

    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Q4
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number =", largest)

# Q5
elif choice == 5:
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    m1 = float(input("Enter marks of Subject 1: "))
    m2 = float(input("Enter marks of Subject 2: "))
    m3 = float(input("Enter marks of Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3

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

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

else:
    print("Invalid Choice!")
