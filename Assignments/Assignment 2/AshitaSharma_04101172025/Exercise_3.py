# Generated from: Exercise_3.ipynb
# Converted at: 2026-06-04T14:23:10.924Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

n = int(input("How many terms? "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b