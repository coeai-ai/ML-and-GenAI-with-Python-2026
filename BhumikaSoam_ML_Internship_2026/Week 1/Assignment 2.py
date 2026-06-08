#1-sum of first 10 natural nums
sum = 0
num = 1
while num < 11:
    print(num ,"\t")
    sum+=num
    num+=1
print("the sum is : ",sum)

#2-factorial
num = int(input("Enter the number for factorial : "))
factorial = 1
if num < 0:
    print("factorial isnt possible!")
else:
    for x in range(1,num+1):
        factorial*=x
print("factorial : ",factorial)

#3-fibonacci
prev = 0
curr = 1
print("elements of fibonacci series : ")
print(prev,"\n",curr)
for x in range(10):
    prev,curr = curr, prev+curr
    print(curr)

#4-Student result system
name = input("Student's Name : ")
section = input("Section : ")
rollno = input ("Roll Number : ")
eng = int(input("Marks in English : "))
math = int(input("Marks in Maths : "))
sci = int(input("Marks in Science : "))
total = E + M + S
per = (total/300)*100
print("percentage : ", per, "%")
if per > 90 :
    print("grade : A")
elif per > 80:
    print("grade : B")
elif per > 70:
    print("grade : C")
elif per > 60:
    print("grade : D")
else :
    print("grade : E")