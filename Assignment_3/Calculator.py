def add(a, b):
    print("Result =", a + b)

def subtract(a, b):
    print("Result =", a - b)

def multiply(a, b):
    print("Result =", a * b)

def divide(a, b):
    print("Result =", a / b)

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    add(num1, num2)

elif choice == 2:
    subtract(num1, num2)

elif choice == 3:
    multiply(num1, num2)

elif choice == 4:
    divide(num1, num2)

else:
    print("Invalid Choice")