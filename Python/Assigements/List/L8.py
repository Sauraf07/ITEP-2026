li = [1,3,5,7,10]
print(li)
for i in range(len(li)):
    if li[i]%5==0:
        li[i]=0
print(li)