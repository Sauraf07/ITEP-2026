def binarySearch():
    num = [1, 2, 3, 4, 5, 6, 7]
    print(num)

    n = int(input("Enter a number : "))

    start = 0
    end = len(num) - 1

    while start <= end:
        mid = (start + end) // 2

        if num[mid] == n:
            print(f"Found element at index {mid}")
            return
        elif n > num[mid]:
            start = mid + 1
        else:
            end = mid - 1

    print("Element not found")

binarySearch()