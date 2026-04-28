'''
Arguments:
    1.Mutable
    2.Immutable

'''
def f1(a, b=0):
    b = b+1
    print(f"inside f1 a : {a} b : {b}")
f1(10)
f1(10)
f1(10)