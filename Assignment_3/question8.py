name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved successfully.")