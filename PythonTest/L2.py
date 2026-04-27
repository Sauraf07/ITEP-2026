'''Find the union of two list '''
list1 = [1,2,4,5,6,7,9,12]
list2 = [2,5,7,9,12]
print(list1)
print(list2)
n1 = len(list1)
n2 = len(list2)
result = []
i =  j = 0
while i<n1 and j<n2:
    if list1[i] <list2[j]:
        if not result or result[-1] != list1[i]:
            result.append(list1[i])
        i += 1
    elif list2[j] < list1[i]:
        if not result or result[-1] != list2[j]:
            result.append(list2[j])
        j += 1
    else:
        if not result or result[-1] != list1[i]:
            result.append(list1[i])
        i +=1 
        j +=1
while j < n2:
    if not result or result[-1] != list2[j]:
        result.append(list2[j])
    j += 1

while i < n1:
    if not result or result[-1] != list1[i]:
        result.append(list1[i])
    i += 1

print(f"Union List : {result}")