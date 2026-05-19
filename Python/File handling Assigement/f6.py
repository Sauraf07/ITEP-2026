'''
6. Replace Specific Word

Using r+ mode:

Replace every occurrence of:

Python

with:

Java
'''
try:
    with open('data/replace_word.txt', 'r+') as f:
        content = f.read()
        modified_content = content.replace('Python', 'Java')
        
        f.seek(0)
        f.write(modified_content)
        f.truncate()  
        
        print("Modified file content:")
        print(modified_content)
except Exception as e:
    print("An error occurred:", e)