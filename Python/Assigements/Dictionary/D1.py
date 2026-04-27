data={"a":1,"b":2,"c":1,"d":3}
result={}
for key,value in data.items():
    if value in result:
        result[value]=result[value]+[key]
    else:
        result[value]=[key]
for value,keys in result.items():
    if len(keys)>1:
        print(keys)