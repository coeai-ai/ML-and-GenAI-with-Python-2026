##question1
addition= 0
for i in range(1,11):
    addition+= i
print(addition)

##question2
a = int(input("Enter the number: "))
n=1
for i in range(1,a+1):
    n= n*i
print(n)

##question3
a = int(input("Enter the number: "))
prev = 0
curr = 1
for i in range(0,a+1):
    if i==0:
        print(0, end=" ")
    elif (i==1):
        print(1, end=" ")
    else:   
        nxt = prev + curr
        print(nxt, end=" ")
        prev = curr
        curr = nxt      



# question4
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))  
if (a>b) and (a>c):
    print("The greatest number is: ", a)
elif (b>a) and (b>c):
    print("The greatest number is: ", b)
else:    print("The greatest number is: ", c)   


#question5
a = input("Enter the name: ")
b= int(input("Enter the marks:"))
c= int(input("Enter the maximum marks:"))
percentage = (b/c)*100
print("The percentage is: ", percentage)
if percentage>=90:
    print("Grade: A")
elif percentage>=80:
    print("Grade: B")
elif percentage>=70:
    print("Grade: C")
elif percentage>=60:
    print("Grade: D")
else:    print("Grade: F")  

