
'''2. Count Characters

Using r+ mode:

Open a file
Read all contents
Print total number of characters
'''
with open('data/file.txt', 'r+') as f:
    content = f.read()
    character_count = len(content)
    print(f'Total number of characters: {character_count}')
    