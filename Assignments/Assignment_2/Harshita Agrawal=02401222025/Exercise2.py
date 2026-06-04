# Program to calculate the factorial of a number
f=int(input("Enter a number: "))
j=f-1

# Calculating factorial using a while loop
while j>=1:
    f=f*j
    j-=1
print("Factorial of the number is:", f)