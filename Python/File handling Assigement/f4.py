'''
4. Append User Input

Using a+ mode:

Ask user for a sentence
Append it to a file
Display complete file content
'''
user_input = input("Enter a sentence to append: ")
with open('data/appended.txt', 'a+') as f:  
    f.write(user_input + '\n')  
    f.seek(0)  
    content = f.read()  
    print("Complete file content:")
    print(content)
    