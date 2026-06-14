def in_num():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    return num1,num2 
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if(b==0):
        print("Error!! Can't be divided by zero")
        return
    return a/b

# Display operations
while True:
    print("\n CALCULATOR\n1.Addition\n2.Multiply\n3.Subtract\n4.Divide\n5.Exit")
    choice=int(input("Enter your choice(1/2/3/4/5): "))
    if choice==1:
        num1,num2=in_num()
        print("Result =", add(num1, num2))
    elif choice==2:
        num1,num2=in_num()
        print("Result =", multiply(num1, num2))
    elif choice==3:
        num1,num2=in_num()
        print("Result =", subtract(num1, num2))
    elif choice==4:
        num1,num2=in_num()
        print("Result =", divide(num1, num2))
    elif choice==5:
        print("\nExited successfully")
        print("*****THANK YOU*****")
        break
    else:
        print("\n!!!!!Invalid choice!!!!!")