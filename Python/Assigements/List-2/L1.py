lst = [1,2,3,4,5]
print(lst)
n = len(lst)

if n == 1:
    print(f"Peak element found at {0} => {1}")
elif n == 2:
    if lst[0] > lst[1]:
        print(f"Peak element found at {0} => {1}")    
    elif lst[1] > lst[0]:
        print(f"Peak element found at {1} => {1}")
    else:
        print(f"Peak element not found => {0}")    
elif n > 2:
    # check for last element
    if lst[n-1] > lst[n-2]:
        print(f"Peak element found at {n-1} => 1")
    elif lst[0] > lst[1]:
        print(f"Peak element found at {0} => 1") 
    else:
        for i in range(1,n-1):
            if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
                print(f"Peak element found at : {i} => 1")
                break
        else:
            print(f"Peak element not found => {0}")