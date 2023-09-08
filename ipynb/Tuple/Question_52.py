from operator import itemgetter
l = [('Tom',19,80),('John',20,90),('Jony',17,91),('Jony',17,93)]
print(sorted(l,key = itemgetter(0,1,2)))