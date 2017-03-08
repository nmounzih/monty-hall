import random


def game_simulation():
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
    


game_simulation()
