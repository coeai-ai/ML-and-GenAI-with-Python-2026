# Generated from: Exercise_2.ipynb
# Converted at: 2026-06-04T14:23:06.574Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "=", factorial)