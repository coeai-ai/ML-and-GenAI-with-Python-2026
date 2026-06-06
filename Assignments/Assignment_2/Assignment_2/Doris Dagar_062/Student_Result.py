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


# Display Grades
print("\n**************** RESULT *****************")

if (percentage>=92):
    print("Grade: A")
    print("Remarks: Excellent!!")
elif(percentage>=82 and percentage<92):
    print("Grade: B")
    print("Remarks: Good :)")
elif(percentage>=70 and percentage<82):
    print("Grade: C")
    print("Remarks: You can do better")
elif(percentage>=55 and percentage<70):
    print("Grade: D")
    print("Remarks: Try hard next time")
else:
    print("Grade: F")
    print("Remarks: Fail")