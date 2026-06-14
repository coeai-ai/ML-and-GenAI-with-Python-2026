# Reading data from students.txt
with open("students.txt", "r") as file:
    print("\nStudent Details:")
    print(file.read())