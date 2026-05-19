'''
3. Create and Write

Using w+ mode:

Create a file named notes.txt
Write 5 lines into it
Read and display all lines
'''
with open('data/notes.txt', 'w+') as f:
    lines = [
        "Line 1: This is the first line.\n",
        "Line 2: This is the second line.\n",
        "Line 3: This is the third line.\n",
        "Line 4: This is the fourth line.\n",
        "Line 5: This is the fifth line.\n"
    ]
    f.writelines(lines)
    f.seek(0)
    content = f.read()
    print(content)