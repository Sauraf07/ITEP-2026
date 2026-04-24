data = {"a": 1, "b": 2, "c": 1, "d": 3}
result = []
for i in data.items():
    print(i)
    for j in range(len(data)):  
        if data.get(i) == data.get(j):
            result.append(data.get())

      
print(result)