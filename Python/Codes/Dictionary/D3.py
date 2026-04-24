c = {"id": 100, "name": "Atul", "contact": "9009111322","age": 21}
for key in c.keys():
    print(key,":",c[key])

print("Getting Values... ")

for value in c.values():
    print(value)

for key,value in c.items():
    print(f"{key} : {value}")