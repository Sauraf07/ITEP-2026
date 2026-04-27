'''Invert a Dictionary (Handle Duplicates)

Swap keys and values. If values repeat, store keys in a list.

Example:

data = {"a": 1, "b": 2, "c": 1}

👉 Output:

{1: ['a', 'c'], 2: ['b']}
'''
data = {"a":1, "b":2,"c":1}
dublicate = {}
for key in data:
    if data[key] in dublicate:
        dublicate[data[key]].append(key)
    else:
        dublicate[data[key]] = [key]
print(dublicate)