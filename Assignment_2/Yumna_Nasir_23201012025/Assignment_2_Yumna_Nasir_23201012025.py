#ASSIGNMENT 2

#1. Find sum of first 10 natural numbers.
def findSum(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum
if __name__ == "__main__":
    n = int(input("Enter number:"))
    print(findSum(n))

#2. Find factorial of a number.
n = int(input("Enter number:"))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)

#3. Print Fibonacci Series.
n = int(input("Enter number:"))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#4. Find largest among 3 numbers.
a = int(input("\nEnter number 1:"))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))
if a >= b and a >= c:
    res = a
elif b >= a and b >= c:
    res = b
else:
    res = c
print(res)

#5. Grade Calculator.
name = input("Enter student name:")
cls = input("Enter class:")
roll = int(input("Enter roll number:"))
print("Enter Marks Obtained in 5 Subjects: ")
total1 = int(input("Enter marks for subject 1:"))
total2 = int(input("Enter marks for subject 2:"))
total3 = int(input("Enter marks for subject 3:"))
total4 = int(input("Enter marks for subject 4:"))
total5 = int(input("Enter marks for subject 5:"))
tot = total1 + total2 + total3 + total4 + total4
print("Total marks is", tot)
per= tot/500*100
print("Percentage is", per)
avg = tot / 5
print("Average is", avg)
if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")


