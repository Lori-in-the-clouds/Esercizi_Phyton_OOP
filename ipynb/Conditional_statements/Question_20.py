def funcion(t1,t2):
    if len(t1) > len(t2):
        print(t1)
    elif len(t2) > len(t1):
        print(t2)
    else:
        print(t1+t2)

funcion("one","three")