def double(list_tup):
    new = []
    for i in list_tup:
       new.append((i[0],i[1],i[2]*2))
    return new



l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(double(l))



