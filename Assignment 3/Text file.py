# Program to create a text file and store student details

#Taking student details as input
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
course = input("Enter Course: ")
marks = input("Enter Marks: ")

# Creating and opening a text file in write mode
with open("student_details.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Marks: {marks}\n")

print("Data saved successfully.")