'''
7. Copy File Content

Using file modes:

Read one file
Write contents into another file
8. Line Number Writer

Using a+ mode:

Append lines like:

1. Apple
2. Mango
3. Banana

Automatically maintain numbering.
'''
try:
    with open('data/source.txt', 'r') as source_file:
        content = source_file.read()
        
    with open('data/destination.txt', 'w') as dest_file:
        dest_file.write(content)
        
    print("File content copied successfully.")
except Exception as e:
    print("An error occurred while copying file:", e)