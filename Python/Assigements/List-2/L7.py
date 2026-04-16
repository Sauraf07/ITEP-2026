lst = [1,2,4,5,3,2,6,8,1]
element = 1
counter = 0
for item in lst:
    if element == item:
        counter += 1

print(f"Element found {counter} times "if counter else "Element not found ") 