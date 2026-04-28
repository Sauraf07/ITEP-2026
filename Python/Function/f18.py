def DataEncap():
    counter = 100
    def increment():
        nonlocal counter
        counter = counter + 1
        print(f"Inside increment : {counter}")
    def decrement():
        nonlocal counter
        counter = counter -1
        print(f"Inside decrement : {counter}")
    return increment,decrement

increment, decrement = DataEncap()
increment()
increment()
increment()
decrement()
decrement()