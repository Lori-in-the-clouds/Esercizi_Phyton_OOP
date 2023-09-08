count=0
index=0

while index < 300:
    if index % 17 ==0:
        print(index)
        count = count + 1

    index = index + 1

print("total numbers {}".format(count))