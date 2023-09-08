l = [12,24,35,70,88,120,155]

new = list((i for i in l if i % 5 != 0 and i % 7 != 0))
print(new)