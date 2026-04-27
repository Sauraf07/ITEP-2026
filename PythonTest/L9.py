'''
Sort Dictionary by Value

Sort dictionary in ascending order of values.

Example:

data = {"a": 3, "b": 1, "c": 2}
'''
data = {"a": 1, "b": 2, "c": 1}

result = {}

for key in data:
    value = data[key]
    if value in result:
        result[value].append(key)
    else:
        result[value] = [key]
print(result)  