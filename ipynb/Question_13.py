def four_copies(string :str):
    result="";
    for x in range(4):
        result+=string[-2:]

    return result

print(four_copies("Python"))
