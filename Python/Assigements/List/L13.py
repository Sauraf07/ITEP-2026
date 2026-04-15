arr = [1,2,3,4,5,4,6,2,1]
count = {}
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)