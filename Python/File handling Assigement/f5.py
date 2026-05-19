'''

5. Cursor Position Practice
Using tell() and seek():
Write data to a file
Print cursor position after each operation
Move cursor to different locations
'''
try:
    with open('data/cursor_practice.txt', 'w+') as f:
        f.write("Hello, World!\n")
        print("Cursor position after writing:", f.tell())
        
        f.seek(0)
        print("Cursor position after seeking to start:", f.tell())
        
        content = f.read()
        print("File content:")
        print(content)
        print("Cursor position after reading:", f.tell())
        
        f.seek(5)
        print("Cursor position after seeking to 5:", f.tell())
except Exception as e:
    print("An error occurred:", e)
