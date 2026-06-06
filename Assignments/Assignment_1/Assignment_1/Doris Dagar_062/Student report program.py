'''Let us say the details are:
1. Name 
2. Marks of Physics, Chemisrty, Maths, English, Computer Science'''

#Input Name
n=str(input("Enter Name of the student: "))

#Input Marks (Out of 100)
p=int(input("Enter Physics marks: "))
c=int(input("Enter Chemistry marks: "))
m=int(input("Enter Maths marks: "))
e=int(input("Enter English marks: "))
cs=int(input("Enter Computer Science marks: "))

#Calculate the total Marks
total=p+c+m+e+cs

#Calculate the percentage
percentage=(total/500)*100

#Print the values of total marks obtained and the percentage
print("\n********************* REPORT *************************")
print("\nTotal marks obtained by",n,"is: ",total,"/500")
print("Percentage is: ",round(percentage,2),"%")