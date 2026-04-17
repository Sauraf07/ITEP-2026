# intersection
l1 = [1,2,4,5,6,7,9,10]
l2 = [1,2,3,4,5,9,11]
n1 = len(l1)
n2 = len(l2)
result = []
i = j =  0
print(f"L1 {l1}")
print(f"L2 {l2}")
while i < n1 and j < n2:
    if l1[i]==l2[j]:
        if not result or result[-1]!=l1[i]:
            result.append(l1[i])
        i += 1
        j += 1
    elif l1[i] < l2[j]:
        i += 1
    else:
        j += 1
print(f"Result : {result}")
