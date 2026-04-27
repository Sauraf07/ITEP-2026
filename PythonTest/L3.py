'''Find the intersection to two list '''
list1 = [1,2,5,6,7,9,11,13]
list2 = [1,2,6,8,9,10]
print(f"List1 :  {list1}")
print(f"List2 : {list2}")
n1 = len(list1)
n2 = len(list2)
result = []
i = j = 0
while i < n1 and j < n2:
    if list1[i] == list2[j]:
        if len(result) == 0 or result[-1] != list1[i]:
            result.append(list1[i])
        i += 1
        j += 1    

    elif list1[i] < list2[j]:    
        i += 1
    else:
        j += 1
print(f"Intersection : {result}")