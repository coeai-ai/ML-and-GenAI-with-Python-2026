19101172025
SHUBHANGI SINHA

#QUESTION 1
print(sum(range(1, 11)))

#QUESTION 2
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

#QUESTION 3
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

#QUESTION 4
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))

#QUESTION 5 (Assuming each subject's exam is of 100 marks)
name = input()
roll = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print(name)
print(roll)
print(percentage)
print(grade)