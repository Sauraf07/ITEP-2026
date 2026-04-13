"""
x
xx
xxx
xxxx
xxx
xx
x
"""
n= int(input("enter the value of n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("x",end="")
    print()
for i in range(1,n):
    for j in range(n,i,-1):
        print("x",end="")
    print()