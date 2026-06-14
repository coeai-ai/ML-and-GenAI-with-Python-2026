# Program to read data from a file

try:
    with open("student_details.txt", "r") as file:
        data = file.read()

    print("Contents of the file:")
    print(data)

except FileNotFoundError:
    print("Error: File does not exist.")