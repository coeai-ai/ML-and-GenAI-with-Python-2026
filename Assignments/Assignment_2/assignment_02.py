#ques 1 : sum of first 10 natural number 
sum = 0
for i in range(1, 11):
    sum += i
    i += 1 
print (sum)

#ques 2 : factorial of number 
num = int(input("Enter a number you need factorial of: "))
fact = 1
if num == 0:
    print("factorial of 0 is 1 ")
elif num == 1:
    print("factorial of 1 is 1 ")
else:
    for i in range (1, num +1):
     fact *= i
    i += 1 
    print("factorial of", num, "is", fact)

#ques 3 : fibonacci series
def fibonacci(nterms):
    if nterms <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return
    a, b = 0, 1
    if nterms == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, nterms):
            c = a + b
            a = b
            b = c
            print(c)
nterms = int(input("Enter the number of terms you want: "))
fibonacci(nterms)

#ques 4 : student result system
def main():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    subjects = ["Physics", "Chemistry", "Math", "Biology", "English"]
    marks = []
    print("\nEnter marks for the following subjects (out of 100):")
    for sub in subjects:
        score = float(input("  {}: ".format(sub)))
        marks.append(score)
    total_marks = 0
    for m in marks:
        total_marks = total_marks + m
    percentage = (total_marks / (len(subjects) * 100)) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "Fail"
    print("\n" + "="*35)
    print("         FINAL RESULT")
    print("="*35)
    print("Student Name : {}".format(name))
    print("Roll Number  : {}".format(roll_no))
    print("-" * 35)
    print("Total Marks  : {} / {}".format(total_marks, len(subjects) * 100))
    print("Percentage   : {:.2f}%".format(percentage))
    print("Grade        : {}".format(grade))
    print("="*35)

main()