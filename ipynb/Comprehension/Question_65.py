import random
new = [(i for i in range(201) if i % 5 == 0 and i % 7 == 0)]
print(random.choice(new))