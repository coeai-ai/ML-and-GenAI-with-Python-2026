# Question1
sum = 0
for i in range(1,10):
  sum = sum+i
print(sum)

# Question2
num = 4
fact = 1
for i in range(1,num+1):
  fact = fact * i
print(fact)

# Question3
# n = int(input("Enter Number:"))
# fibo = [0,1]
# for i in range(2,n):
#   fibo.append(fibo[i-1]+fibo[i-2]) 
# print(fibo)


# Question4
# num1 = int(input("Enter Number1 : "))
# num2 = int(input("Enter Number2 : "))
# num3 = int(input("Enter Number3 : "))

# if(num1 > num2 and num1>num3):
#   print("num1 is largest")
# elif(num2> num3 and num2> num1):
#   print("num2 is largest")
# else:
#   print("num3 is largest")

#Question5

name = input("Name of the Student:")
Roll_no = int(input("Roll no. of Student :"))
sub1 = float(input("Marks of Sub1 : "))
sub2 = float(input("Marks of Sub2 : "))
sub3 = float(input("Marks of Sub3 : "))
sub4 = float(input("Marks of Sub4 : "))

total = sub1+sub2+sub3+sub4
percentage = total/4

if(percentage >=85):
  print("Grade A")
elif(percentage>=60):
  print("Grade B")
else:
  print("Grade C")






