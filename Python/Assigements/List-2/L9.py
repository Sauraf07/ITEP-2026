lst = [0,1,2,1,2,1,0,1,0,2,0,1,0,2]
i = 0
c = 0
j = len(lst) - 1
while c<j:
    if lst[c] == 0:
        lst[i],lst[c]=lst[c],lst[i]
        i+=1
        c+=1
    elif lst[c] == 1:
        c += 1
    else:
        lst[c],lst[j]= lst[j],lst[c]
        j -= 1
print(lst)