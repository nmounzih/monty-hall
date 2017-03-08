import random


def game_simulation():
    goat_prizes = 0
    car_prizes = 0
    for x in range(1, 1000):
        door_car = []
        door_first_pick = []
        poss_goat = []
        door_goat = []
        doors = [1, 2, 3]
        car = random.choice(doors)
        door_car.append(car)
        pick = random.choice(doors)
        door_first_pick.append(pick)
        for num in doors:
            if num not in door_car and num not in door_first_pick:
                poss_goat.append(num)
        door_goat.append(random.choice(poss_goat))
        if door_first_pick == door_car:
            car_prizes += 1
        else:
            goat_prizes += 1
    print(goat_prizes)
    print(car_prizes)




game_simulation()
