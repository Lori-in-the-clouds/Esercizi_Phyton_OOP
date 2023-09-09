l = [12,24,35,70,88,120,155]
print(list((x for (i,x) in enumerate(l) if i % 2 != 0)))