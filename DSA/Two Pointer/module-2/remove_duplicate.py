def moving_duplicate(num):
    p =0
    for i in range(1,len(num)):
        if num[p] != num[i]:
            p += 1
            num[p] = num[i]
    return p + 1

num = [1,1,2,2,3]
k = moving_duplicate(num)
print(num[0:k])
