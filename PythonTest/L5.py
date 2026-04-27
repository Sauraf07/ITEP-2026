'''Find Duplicate Values
   Given a dictionary, find keys that have the same values.
   Example:
   data = {"a": 1, "b": 2, "c": 1, "d": 3}
'''
data = {"a":1,"b":2,"c":1,"d":3}
dublicate = {}
for key in data:
    if data[key] in dublicate:
        dublicate[data[key]].append(key)
    else:
        dublicate[data[key]] = [key]
for key in dublicate:
    if len(dublicate[key]) > 1:
        print(dublicate[key])