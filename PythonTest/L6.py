''' program to insert an element at specifi index'''
l1 = [1,2,3,4,5]
index = 2
element = 10
for i in range(len(l1)):
    if i == index:
        l1.insert(i,element)
print(l1)
