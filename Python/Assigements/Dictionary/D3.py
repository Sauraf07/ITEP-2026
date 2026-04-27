words = ['hi','hello','hey','python']
result = {}
for item in words:
    length = len(item)
    if length in result:
        result[length] = result[length] +[item]
    else:
        result[length] = [item]
print(result)
