def valid_Plandrome(s):
    def isPlandrome(left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) -1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return isPlandrome(left+1,right) or isPlandrome(left,right-1)
    return True

s = 'raceacar'
result = valid_Plandrome(s)
print(result)