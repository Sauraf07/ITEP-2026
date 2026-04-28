x = [1,2,3,4,5]
result = list(filter(lambda n: not n%2,x))
print(result)

result = list(filter(lambda n: n%2 , x))
print(result)