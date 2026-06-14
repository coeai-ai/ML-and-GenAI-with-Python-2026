name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll_no)

file.close()

print("Student details saved successfully.")