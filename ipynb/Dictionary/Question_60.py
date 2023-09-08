string = "Hello World!"
v = {}
for c in string:
    if c in v:
        v[c] += 1
    else:
        v[c] = 0

print(v)
