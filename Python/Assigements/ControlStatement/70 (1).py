"""
* * * * * 
 * * * * 
  * * * 
   * * 
    *
"""
n= int(input("enter the value of n"))
for i in range(n,0,-1):
    for s in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()