'''1. Read and Modify First Word

Using r+ mode:

Create a file containing:

Hello World
Replace Hello with Hi
'''
with open('data/file.txt', 'r+') as f:
    content = f.read()
    modified_content = content.replace('Hello', 'Hi')
    f.seek(0)
    f.write(modified_content)
    f.truncate()  

with open('data/file.txt', 'r') as f:
    print(f.read())
