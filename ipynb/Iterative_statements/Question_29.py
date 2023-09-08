import math

def bynary_search2 (list,n):
    top = len(list)-1
    bottom = 0
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top+bottom)/2.0))
        if n>list[mid]:
            bottom = mid + 1
        elif n < list[mid]:
            top = mid - 1
        else:
            index = mid
    return index


l = [2,5,7,9,11,17,222]
print(bynary_search2(l,11))

