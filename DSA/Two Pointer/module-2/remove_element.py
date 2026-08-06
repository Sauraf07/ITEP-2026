def remove_element(num,val):
    p =0
    for i in range(len(num)):
        if num[i] != val:
            num[p] = num[i]
            p += 1
    return p

num = [3,1,3,4,6,7,8,1,3]
val = 3
print(num)
k = remove_element(num,val)
print(num[0:k])