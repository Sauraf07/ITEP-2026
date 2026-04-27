'''Reverse the list in place'''
l1 = [1,2,5,5,7,9,6,2]
for i in range(len(l1)//2):
    l1[i], l1[len(l1)-1-i] = l1[len(l1)-1-i], l1[i]
print(l1)