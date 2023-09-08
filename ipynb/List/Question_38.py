def simultaneously(list1,list2):
    if len(list1) != len(list2):
        return None
    new = []
    for i in range(len(list1)):
        new.append(list1[i]*list2[i])
    return new

print(simultaneously([1,2,3], [4,5,6]))