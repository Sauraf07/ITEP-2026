lst = [1,2,3,4,5,6,7,8,9,10]
s = 15
csum = 0
flag = False
for i in range(len(lst)-1):
    csum = lst[i]
    for j in range(i+1,len(lst)):
        csum = csum + lst[j]
        if csum == s:
            flag = True
            break
        elif csum >s:
            break
    if flag:
        break
print(f"{i+1},{j+1}" if flag else "{-1}")
