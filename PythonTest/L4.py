'''Find the occurrence of all the numbers in a list'''
l1 = [1,2,5,5,7,9,1,2]
count = {}
for i in l1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
