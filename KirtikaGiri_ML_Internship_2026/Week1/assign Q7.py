
# STUDENTS DETAILS
Class=int(input("class-"))
sctn=str(input("Section- ")) 
name=str(input("Student Name- ") )
roln=int(input("Student_Roll_Number- "))

#STUDENTS MARKS
marks=[]
for i in range(5):
    print("\nSubject entry- " + str(i+1))
    x= str(input("sunject name- "))
    y=float(input("enter marks- "))

    marks.append(y)

print("Total Marks- " ,sum(marks))
print("Percentage- ", sum(marks)/5)

