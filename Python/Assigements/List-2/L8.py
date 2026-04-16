lst = [0,1,2,1,2,1,0,1,0,2,0,1,0,2]
zero_count = one_count = two_count = 0
print(f"Before {lst}")
for element in lst:
    if element == 0:
        zero_count += 1
    elif element == 1:
        one_count += 1
    else:
        two_count =+ 1
lst = [0]*zero_count + [1]*one_count + [2] *two_count
print(f"After {lst}")