
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
# ==============================================================================================


def head_location(location_dict_ghably, move_key, first_locations, dict_get_from_apple_location):
    global snake_wide
    for item in location_dict_ghably:
        if (location_dict_ghably[item][0] == 3) and (location_dict_ghably[item][1] == 2):
            snake_neck = list(item)
        if location_dict_ghably[item][0] == 2:
            new_head = list(item)
            new_head_z = new_head.copy()
    if move_key == 'b\'w\'':
        new_head[0] -= 1
    if move_key == 'b\'s\'':
        new_head[0] += 1
    if move_key == 'b\'a\'':
        new_head[1] -= 1
    if move_key == 'b\'d\'':
        new_head[1] += 1

    if not(tuple(new_head) in first_locations):
        return 'game over', None

    if location_dict_ghably[tuple(new_head)][0] == 2:
        # cant back the head
        # breakpoint()
        e1 = new_head_z[0] - snake_neck[0]
        e2 = new_head_z[1] - snake_neck[1]
        if e1 == 1:
            new_head[0] += 1
        if e1 == -1:
            new_head[0] -= 1
        if e2 == 1:
            new_head[1] += 1
        if e2 == -1:
            new_head[1] -= 1
    if new_head == snake_neck:
        new_head = new_head_z.copy()
        e1 = new_head_z[0] - snake_neck[0]
        e2 = new_head_z[1] - snake_neck[1]
        if e1 == 1:
            new_head[0] += 1
        if e1 == -1:
            new_head[0] -= 1
        if e2 == 1:
            new_head[1] += 1
        if e2 == -1:
            new_head[1] -= 1
    if not(tuple(new_head) in first_locations):
        return 'game over', None
    if location_dict_ghably[tuple(new_head)][0] == 3:
        if location_dict_ghably[tuple(new_head)][1] == snake_wide:
            dict_get_from_apple_location[tuple(new_head)] = [2, 1]
            return dict_get_from_apple_location, None
        else:    
            return 'game over', None
    # new_locations_dict = first_locations.copy()
    if location_dict_ghably[tuple(new_head)][0] == 4:
        dict_get_from_apple_location[tuple(new_head)] = [2, 1]
        return dict_get_from_apple_location, 'true'
    dict_get_from_apple_location[tuple(new_head)] = [2, 1]
    return dict_get_from_apple_location, None
# ==============================================================================================


def snake_body(location_dict_ghably, arg, new_locations):
    saver = location_dict_ghably.copy()
    global snake_wide
    for item in location_dict_ghably:
        if location_dict_ghably[item][1] >= 2:
            body_position = location_dict_ghably[item][1]
            for item2 in saver:
                if saver[item2][1] == (body_position - 1):
                    new_locations[item2] = [3, body_position]
                if (arg == 'true') and (body_position == snake_wide) and (saver[item2][1] == snake_wide):
                    snake_wide += 1
                    new_locations[item2] = [3, snake_wide]
    return new_locations
# ==============================================================================================


def final_list(new_locations, fig_list_1):
    final_fig = []
    for item in fig_list_1:
        for item2 in new_locations:
            if tuple(item) == item2:
                if new_locations[item2][0] == 1:
                    final_fig.append('#')
                    # print('\U0001f3fb')
                if new_locations[item2][0] == 2:
                    final_fig.append('0')
                if new_locations[item2][0] == 3:
                    final_fig.append('-')
                if new_locations[item2][0] == 4:
                    final_fig.append('@')
    return final_fig
# ==============================================================================================


def draw(final):
    global game_size
    counter = 0
    for item in final:
        counter += 1
        if (counter % game_size) == 0:
            print(item)
        else:
            print(item, end='')
# ==============================================================================================

recog = 0
def go_away():
    global recog
    recog = 1
# ==============================================================================================


def move_saver(arg):
    if arg == 'b\'w\'':
        move_be = 'b\'s\''
        return move_be
    if arg == 'b\'s\'':
        move_be = 'b\'w\''
        return move_be
    if arg == 'b\'a\'':
        move_be = 'b\'d\''
        return move_be
    if arg == 'b\'d\'':
        move_be = 'b\'a\''
        return move_be
# ==============================================================================================


while True:
    snake_wide = 2
    game_size = 10
    fig_list = []
    difficulty = int(input('enter the difficulty of game(from 1 to 5): '))
    timing = 1.60 - (difficulty * 0.20)

    locations, first_locations_copy = game_earth()
    old_location_dict = locations.copy()
    locations, apple_tuple = apple_location(old_location_dict, locations)
    old_location_dict = locations.copy()

    fig_list = list_maker(fig_list)
    fig_list_z = fig_list.copy()
    fig_list = final_list(locations, fig_list_z)
    draw(fig_list)

    print(" \n \n this is the game earth, for start press keys ")

    f_counter = 1
    ff_counter = 1
    b_move = 'b\'a\''
    while True:
                move = None
                # try:
                if ff_counter == 1:
                    move = repr(readchar()).lower()
                    ff_counter = 2
                else:
                    t = Timer(timing, go_away)
                    t.start()
                    if recog != 1:
                        move = repr(readchar()).lower()
                        while move == b_move:
                            move = repr(readchar()).lower()
                    t.cancel()
                # except:
                recog = 0
                free1 = 1
                # finally:
                locations, apple = head_location(old_location_dict, move, first_locations_copy, locations)

                if locations == 'game over':
                    print("GAME OVER \n play again ")
                    break

                locations = snake_body(old_location_dict, apple, locations)

                if apple == 'true':
                    locations, apple_tuple = apple_location(old_location_dict, locations)
                    if locations == "won":
                        print("you Won!! \n  Hora")
                        break
                else:
                    locations[apple_tuple] = [4, 0]

                if f_counter == 1:
                    locations[(1, 1)] = [1, 0]
                    f_counter = 2
                fig_list = final_list(locations, fig_list_z)
                system('cls')
                draw(fig_list)
                b_move = move_saver(move)
                old_location_dict = locations.copy()
                locations = first_locations_copy.copy()

    print('for clean the page and start a new mach press p and for exit press any other key')
    status2 = repr(readchar()).lower()
    if status2 == 'b\'p\'':
        system('cls')
    else:
        break

# 1=empty 2=head 3=body 4=apple
