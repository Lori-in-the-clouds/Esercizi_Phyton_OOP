def longer_than(words,min_lenght):
    new = []
    for i in words:
        if len(i) > min_lenght:
            new.append(i)
    return new

print(longer_than(['hello', 'abc', 'sun', 'moon'], 3))
