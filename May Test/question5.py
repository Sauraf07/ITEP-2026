'''Question 5 — File Handling with Exception Handling
Create a program that:
Asks the user for a filename.
Reads the content of the file.
Displays the total number of:
characters
words
lines
Use proper exception handling for:
FileNotFoundError
PermissionError
Sample Output
Total Characters: 120
Total Words: 25
Total Lines: 5
'''
filename = input("Enter the filename : ")

try:    
    with open(filename,"r") as file:
        content = file.read()
        characters = len(content)
        words = len(content.split())
        lines = len(content.splitlines())

        print(f"Total Characters : {characters}")
        print(f"Total Words : {words}")
        print(f"Total Lines : {lines}")

except FileNotFoundError:
    print("File not found.")
    
except PermissionError:
    print("Permission denied.")

