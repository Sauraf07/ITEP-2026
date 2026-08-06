def moving_zero(num):
    p = 0
    for i in range(len(num)):
        if num[i] != 0:
            num[p],num[i]=num[i],num[p]
            p += 1

numbers = [0,0,0,0,1,5,6,7,0,1,0,0,0,0,3,0,0,0,0,12,0,0]

print(numbers)
moving_zero(numbers)
print(numbers)
