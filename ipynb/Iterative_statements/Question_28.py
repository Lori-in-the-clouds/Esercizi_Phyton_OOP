def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

f=[]
index=0
while True:
    if fibonacci(index) > 10:
        break
    else:
        f.append(fibonacci(index))
    index = index + 1
print(f)