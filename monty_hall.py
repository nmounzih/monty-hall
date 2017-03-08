import random


def main():
    stay_goat_prizes = 0
    stay_car_prizes = 0
    switch_goat_prizes = 0
    switch_car_prizes = 0
    random_goat_prizes = 0
    random_car_prizes = 0
    for x in range(1, 1000):
        door_car = []
        door_first_pick = []
        door_second_pick = []
        poss_goat = []
        door_goat = []
        doors = [1, 2, 3]
        random_pool = []
        car = random.choice(doors)
        door_car.append(car)
        pick = random.choice(doors)
        door_first_pick.append(pick)
        for num in doors:
            if num not in door_car and num not in door_first_pick:
                poss_goat.append(num)
            elif num not in door_goat and num not in door_first_pick:
                door_second_pick.append(num)
        door_goat.append(random.choice(poss_goat))
        if door_first_pick == door_car:
            stay_car_prizes += 1
        else:
            stay_goat_prizes += 1
        door_goat.append(random.choice(poss_goat))
        if door_second_pick == door_car:
            switch_car_prizes += 1
        else:
            switch_goat_prizes += 1
        random_pool.append(door_first_pick)
        random_pool.append(door_second_pick)
        final_choice = random.choice(random_pool)
        if final_choice == door_car:
            random_car_prizes += 1
        else:
            random_goat_prizes += 1

    print("\nWhen you choose to stay: \n")
    print("\tGoats: {}".format(stay_goat_prizes))
    print("\tCars: {}\n".format(stay_car_prizes))
    print("When you choose to switch: \n")
    print("\tGoats: {}".format(switch_goat_prizes))
    print("\tCars: {}\n".format(switch_car_prizes))
    print("When you choose random: \n")
    print("\tGoats: {}".format(random_goat_prizes))
    print("\tCars: {}\n".format(random_car_prizes))


main()
