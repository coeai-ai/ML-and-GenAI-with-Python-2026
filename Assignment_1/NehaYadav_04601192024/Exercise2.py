# print("Sum of first 10 naturnal numbers")
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

# print("factorial of a number")
# num = 5
# fact = 1
# for i in range (1,num+1):
#     fact = fact*i
# print(fact)

# print("fibonacci series")
# a = 0
# b = 1
# for i in range(10):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# print("largest of 3 numbers")
# a = 4
# b = 3
# c = 7
# if a>b and a>c :
#     print(a ,"is the largest number")
# elif b>a and b>c :
#     print(b ,"is the largest number")
# else :
#     print(c ,"is the largest number")

print("student details")
name = input("Enter name: ")
roll_no = input("Enter roll no. : ")
eng = int(input("Enter english marks: "))
hin = int(input("Enter hindi marks: "))
maths = int(input("Enter maths marks: "))
percen = ((eng+hin+maths)/300)*100
if percen > 90 :
    grade = "A+"
elif percen > 80 :
    grade = "A"
elif percen > 70 :
    grade = "B+"
elif percen > 60 :
    grade = "B"
elif percen > 50 :
    grade = "C+"
elif percen > 40 :
    grade = "D"
else :
    grade = "F"

print(name , "has got grade =", grade)