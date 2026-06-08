file = open("student.txt", "r")

data = file.read()

print("Student Details:")
print(data)

file.close()