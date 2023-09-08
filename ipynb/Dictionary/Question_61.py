string =  'hello world! 123'
v={}
v["digit"]=0
v["letters"]=0

for i in string:
    if i.isdigit():
        v["digit"]+=1
    elif i.isalpha():
        v["letters"]+=1
print(v)