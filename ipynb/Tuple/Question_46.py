def remove_element(tup,n):
    if len(tup) < n:
        return None
    return tup[:n]+tup[n+1:]

t = (1, 2, 3, 4, 5, 6, 7, 8)
print(remove_element(t, 2))