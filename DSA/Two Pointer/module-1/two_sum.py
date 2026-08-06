def two_sum(num,target):
    left = 0
    right = len(num) - 1
    while left < right:
        sum = num[left]+ num[right]
        if sum == target:
            return [left+1,right+1]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return False

num = [10,49,10,21]
target = 59
result = two_sum(num,target)
print(result)
