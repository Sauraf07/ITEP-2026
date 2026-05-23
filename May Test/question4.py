'''Question 4 — File Handling (Write and Read)
Write a Python program to:
Create a file named student.txt
Take student details from the user:
Name
Course
Marks
Store the details into the file.
Read the file and display the stored data.
Sample File Content
Name: Amit
Course: Python
Marks: 85
'''

name = input("Enter Student Name : ")
course = input("Enter Course Name : ")
marks = input("Enter Marks : ")

with open("student.txt","w") as file:
    file.write(f"Name : {name}\n")
    file.write(f"Course : {course}\n")
    file.write(f"Marks : {marks}\n")

with open("student.txt","r") as file:
    content = file.read()
    print("Student Details : ")
    print(content)

