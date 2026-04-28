'''
  Positional
  Keyword
  Default
  Variable Length Argument

  Positional --> Default ---> Vairable Length-->Keword--> Varaible Length Keyword
  
'''
def f1(*a):
    sum = 0
    for item in a:
        sum += item
    return sum

result = f1(1,2,3,4,5,6,7)
print(f"Sum : {result}")