'''
Group Words by Length

Group a list of words into a dictionary where key = word length.

Example:

words = ["hi", "hello", "hey", "python","bye"]

👉 Output:

{2: ['hi'], 3: ['hey',"bye"], 5: ['hello'], 6: ['python']}

'''
words = ["hi","hello","hey","python","bye"]
group = {}
for word in words:
    if len(word) in group:
        group[len(word)].append(word)
    else:
        group[len(word)]= [word]
print(group)     