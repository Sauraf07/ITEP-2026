from functools import reduce
x = [1,2,3,4,5]
result = list(map(lambda n: n*n,x))
print(result)

result = reduce(lambda a,b : a+b,x,10)
print(f"Original list : {x}")
print(f"Sum : {result}")