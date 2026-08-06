def dublicate_zero(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            for j in range(len(arr)-1,i,-1):
                arr[j] = arr[j-1]
            arr[j] = 0
            i += 2
        else:
            i += 1

arr = [0,1,2,0,5,6,1,0,2]
print(arr)
dublicate_zero(arr)
print(arr)
