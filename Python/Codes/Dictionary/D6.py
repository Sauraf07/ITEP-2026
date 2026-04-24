data = [1,2,3,4,5,6]
print(data)
result = {item: item*item for item in data}
print(result)

result = {item : "Odd" if item%2 else "Even" for item in data}
print(result)