d = {'a':1,'b':2,'c':3,'d':4,'e':3,'f':1}
result = {value:key for key,value in d.items()}
result = {key:value for key,value in result.items()}
print(result)