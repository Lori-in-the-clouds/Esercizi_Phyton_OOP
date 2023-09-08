def duplicate(list1):
    list2 = []
    for i in list1:
        list2.append(i*2)
    return list2

print(duplicate([1,2,3,4,5]))