# Sum of first 10 natural number 
i = 1
sum = 0
for i in range(1,11):
    sum += i
print(sum)

# Factorial of a number 
n = int(input("number = "))
# for find the factorial
i = 0
fact = 1
for i in range(n):
    fact = fact*(n-i)
print(fact)  

# Fibonacci Series
n = int(input("number = "))
a = 0
b = 1
for i in range(n):
    sum = a+b
    a  = b
    b = sum 
    print(sum) 

# Largest among three number
a = int(input("num a :"))
b = int(input("num b :"))
c = int(input("num c :"))
if(a>=b and a>=c):
    print("a is largest : ",a)
elif(b>=a and b>=c):
    print("b is largest : ",b)
elif(a == b and a==c):
    print("all three are equal")    
else:
    print("c is largest : ",c)    

# Creat a Student result system
Student_name = str(input("Student Name : "))
Enroll = int(input("Enrollment No : "))
College = str(input("College : "))

print("Marks:-")
sub1 = float(input("Subject 1 : "))
sub2 = float(input("Subject 2 : "))
sub3 = float(input("Subject 3 : "))
sub4 = float(input("Subject 4 : "))

total = sub1+sub2+sub3+sub4
persentage = (total/400)*100

print("persentage : ",persentage)
if(persentage >=90):
    print("Grade A")
elif(persentage >= 80):
    print("Grade B")
elif(persentage >=70):
    print('Grade C')
elif(persentage >=60):
    print('Grade D')    
elif(persentage >=40):
    print('Grade E')
else:
    print("Fail")




  
