# map(), filter(), reduce()
# Decorator
def f1(func):
    print(f"F1 executed ")
    func()

def wish():
    print("Good Morning")
f1(wish)