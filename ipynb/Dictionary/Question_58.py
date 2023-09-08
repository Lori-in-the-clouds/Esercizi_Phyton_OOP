def dictionary_1_20_avarage():
    v = {}
    for i in range(1,21):
        v[i]=i**2
    return v

new = dictionary_1_20_avarage()
avarage1 = sum(new.keys())/20
avarage2 = sum(new.values())/20
