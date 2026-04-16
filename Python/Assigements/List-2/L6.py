list = [1,2,3,4,5]
low = 0
high = len(list) - 1
print(list)
while low < high:
    list[low],list[high] = list[high],list[low]
    low += 1
    high -= 1

print(list)