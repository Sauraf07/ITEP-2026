li = [103,20,130,11,1,55,23]
print(li)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] > li[j]:
            li[i],li[j]=li[j],li[i]
print(li)