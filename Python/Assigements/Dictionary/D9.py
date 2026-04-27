d1 = {"a":1,"b":2}
d2 = {"b":3,"c":4}
result = []
for key1 in d1.keys():
    for key2 in d2.keys():
        if key1 == key2:
            result = [key1]
print(result)