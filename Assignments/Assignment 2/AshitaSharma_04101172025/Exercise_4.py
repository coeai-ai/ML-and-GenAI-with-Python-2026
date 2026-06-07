# Generated from: Exercise_4.ipynb
# Converted at: 2026-06-04T14:23:16.064Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)