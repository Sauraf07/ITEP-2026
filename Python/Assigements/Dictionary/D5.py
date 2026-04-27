nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    num = nums[i]
    diff = target - num
    
    if diff in seen:
        print([seen[diff], i])
    
    seen[num] = i