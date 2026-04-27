data = {"a": 1, "b": 2, "c": 1}

result = {}

for key in data:
    value = data[key]
    
    if value not in result:
        result[value] = []
    
    result[value].append(key)

print(result)