# question 1
sum =0
for i in range(1,11):
    sum = sum + i

print("the sum of first 10 number is :",sum)

# question 2
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("the value of factorial is",factorial(4))

# question 3

a,b=0,1
print("the fibonnaci series is ")
for i in range(1,10):
  print(a,end=" ")
  a,b=b,a+b

# # 0 1 1 2 3 5 8


# question 4

def find_max(num1,num2,num3):
    max= num1
    if num2>max:
        max=num2
    if num3>max:
        max=num3

    return max
print(" the maximum number out of 3 number is ",find_max(7,9,98))

# question 5

def result_system(student,mark_sub1,mark_sub2,mark_sub3):
    total_obtained = mark_sub1+mark_sub2+mark_sub3
    percentage = (total_obtained/300)*100
    if percentage>90:
        return"Grade of ",student," is A "
    elif  percentage>80:
        return"Grade of ",student," is B "
    elif percentage > 70:
        return"Grade of ",student," is C "
    elif percentage > 60:
        return"Grade of ",student," is D "
    else :
        return"Grade of", student ," is F "

print(result_system("anshika",89,97,65))
print(result_system("vishu",89,77,69))




