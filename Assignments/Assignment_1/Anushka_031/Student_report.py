# Student Report Program

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

total = mark1 + mark2 + mark3
percentage = total / 3

# Storing student data in dictionary
student = {
    "Name": name,
    "Roll Number": roll_no,
    "Total Marks": total,
    "Percentage": percentage
}

# Display report
print("\n----- Student Report -----")
print("Name:", student["Name"])
print("Roll Number:", student["Roll Number"])
print("Total Marks:", student["Total Marks"])
print("Percentage:", student["Percentage"], "%")