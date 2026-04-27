'''
 find the second maximum and second minimum in the list
'''
l1 = [1,2,6,7,8,9,11,0]
max1 = l1[0]
max2 = l1[0]
min1 = l1[0]
min2 = l1[0]
for i in l1:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i
    if i < min1:
        min2 = min1
        min1 = i
    elif i < min2 and i != min1:
        min2 = i
print(f"Second Maximum : {max2} ")
print(f"Second Minimum : {min2} ")
