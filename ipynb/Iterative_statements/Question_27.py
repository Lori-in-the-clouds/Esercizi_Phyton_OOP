import random

counter1=0
counter2=0

while counter1 != 1000 and counter2 != 1000:
    player1 = random.randint(1, 6)
    player2 = random.randint(1, 6)
    if player1 > player2:
        counter1 = counter1 + 1
    elif player1 < player2:
        counter2 = counter2 + 1

if counter2 == 1000:
    print("The winner is the player 2")
else:
    print("The winner is the player 1")

print("count1 {}, count2 {}".format(counter1,counter2))


