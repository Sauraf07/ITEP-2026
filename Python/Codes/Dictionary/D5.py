data = {10,20,30,4,6,7,5,12,3,5,6,7,8,9,2,0,12,23}
result = {}
for item in data:
    result[item] = result.get(item,0) + 1

'''
for item in data:
    if result.get(item):
        result[item] = result[item]+1
    else:
        result[item] = 1
'''
print(f"Result : {result}")