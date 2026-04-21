'''
List:
   1)Order collection
   2)Allow duplicate elements
   3)Indexing and slicing
   4)Mutable


Tuple:
    1)Order collection
    2)Allow duplicate elements
    3)Indexing and slicing
    4)Immutable
    5)Faster than list

'''

x = ()
print(type(x))
x = (1,2,3)
print(x)
print(x[1])
x = 1,2,3,4,5
print(x)


import sys
x = ()
print(sys.getsizeof(x)) 