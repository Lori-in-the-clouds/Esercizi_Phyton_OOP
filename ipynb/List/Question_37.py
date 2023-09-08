def remove_duplicates(list):
    new = []
    for i in list:
        if i not in new:
            new.append(i)
    return new

l = [1, 2, 3, 2, 1, 3, 4, 4, 5]
print(remove_duplicates(l))