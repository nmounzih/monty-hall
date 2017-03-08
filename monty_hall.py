import random


def stay_game_simulation():
    stay_goat_prizes = 0
    stay_car_prizes = 0
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
            stay_car_prizes += 1
        else:
            stay_goat_prizes += 1
    print("Goats: {}".format(stay_goat_prizes))
    print("Cars: {}\n".format(stay_car_prizes))


def switch_game_simulation():
    switch_goat_prizes = 0
    switch_car_prizes = 0
    for x in range(1, 1000):
        door_car = []
        door_first_pick = []
        door_second_pick = []
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
        for num in doors:
            if num not in door_goat and num not in door_first_pick:
                door_second_pick.append(num)
        if door_second_pick == door_car:
            switch_car_prizes += 1
        else:
            switch_goat_prizes += 1
    print("Goats: {}".format(switch_goat_prizes))
    print("Cars: {}".format(switch_car_prizes))



stay_game_simulation()
switch_game_simulation()
