func = []
for i in range(5):
    func.append(lambda i=i:i)

for item in func:
    print(item())