'''
Example 2:
Input : 
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1
'''


arr = [-5, 7, -3, -4, 9, 10, -1, 11]
k = 0
n = len(arr)
result = [None]*n
for i in range(n):
    if arr[i]>= 0:
        result[k]= arr[i]
        k+=1
for i in range(n):
    if arr[i]<=0:
        result[k]=arr[i]
        k+=1
print(result)
