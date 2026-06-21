n = int(input("Enter the number of students: "))

with open("students.txt", "w") as file:
    for i in range(n):
        print(f"\nStudent {i + 1}")

        name = input("Enter name: ")
        marks = input("Enter marks: ")

        file.write(f"Name: {name}, Marks: {marks}\n")

print("\nStudent details saved successfully.")