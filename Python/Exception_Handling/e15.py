print("At the start")
f = None
try:
    f = open("Python.txt","r")
except FileNotFoundError as e:
    print("File not found")
else:
    print("File found ")
    data = f.read()
    print(data)

finally:
    print("finally block xecuted")
    if f is not None:
        f.close()
print("at the end ")