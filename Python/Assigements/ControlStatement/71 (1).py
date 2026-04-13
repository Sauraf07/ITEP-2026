"""
123456789
 1234567
  12345
   123
    1
"""
n= int(input("enter the value of n"))
for i in range(n,0,-1):
    for s in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i*2)):
        print(j,end="")
    print()