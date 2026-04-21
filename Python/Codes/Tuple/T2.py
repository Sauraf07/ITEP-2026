'''
Tuple Unpacking:
x = (1,2,3)
a,b,c = x
'''
# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)

*a,b,c =  (1,2,3,4,5)
print(a)
print(b)
print(c)

a,*b,c =  (1,2,3,4,5)
print(a)
print(b)
print(c)

a,b,*c =  (1,2,3,4,5)
print(a)
print(b)
print(c)