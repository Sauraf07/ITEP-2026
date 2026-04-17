lst = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(lst)
k = 0
result = [None]*n
for i in range(n):
    if lst[i] >= 0:
        result[k] = lst[i]
        k += 1

for i in range(n):
    if lst[i] < 0:
        result[k]=lst[i]
        k+=1
print(result)
        