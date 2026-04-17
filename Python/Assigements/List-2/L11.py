lst = [1,2,3,4,5]
sum = 5
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == sum:
            print(f"{i+1},{j+1}")
            break