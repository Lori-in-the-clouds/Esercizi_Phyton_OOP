def divisble7_multiple5():
    list = []
    for i in range(200,301):
        if i % 7 == 0 and i % 5 != 0:
            list.append(i.__str__())
    print(",".join(list))


divisble7_multiple5()
