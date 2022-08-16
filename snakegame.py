
from os import system
from random import choice
# import time
# import emoji
from readchar import readchar
from threading import Timer

# ==============================================================================================


def game_earth():
    global game_size
    game_size = int(input('pleas enter the size of earth game: '))
    first_location = {}
    system('cls')
    for item in range(1, game_size+1):
        for item2 in range(1, game_size+1):
            first_location[(item, item2)] = [1, 0]
    copy_list = first_location.copy()
    first_location[(1, 1)] = [3, 2]
    first_location[(1, 2)] = [2, 1]
    return first_location, copy_list
# ==============================================================================================


def list_maker(list1):
    global game_size
    for i in range(1, game_size+1):
        for b in range(1, game_size+1):
            list1.append([i, b])
    return list1
# ==============================================================================================


def apple_location(location_dict_ghably, new_locations):
    save = []
    free = []
    for item in location_dict_ghably:
        if location_dict_ghably[item][0] == 1:
            save.append(item)
    if save == free:
        return 'won', None
    apple1 = choice(save)
    applee = apple1
    new_locations[apple1] = [4, 0]
    return new_locations, applee
