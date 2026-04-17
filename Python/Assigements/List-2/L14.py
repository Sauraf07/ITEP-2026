# union and intersection
l1 = [1,2,3,4,5,6,8,9,10]
l2 = [2,5,8,10,15]
n1 = len(l1)
n2 = len(l2)
result = []
i =  j = 0
while i<n1 and j<n2:
    if l1[i] <l2[j]:
        if not result or result[-1]!=l1[i]:
            result.append(l1[i])
        i += 1
    elif l2[j]<l1[i]:
        if not result or result[-1]!=l2[j]:
            result.append(l2[j])
        j += 1
    else:
        if not result or result[-1]!=l1[i]:
            result.append(l1[i])
        i +=1 
        j +=1
while j < n2:
    if not result or result[-1]!=l2[j]:
        result.append(l2[j])
    j += 1

while i < n1:
    if not result or result[-1]!=l1[i]:
        result.append(l1[i])
    i += 1

print(f"Union : {result}")
