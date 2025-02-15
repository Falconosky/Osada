import random
from  map_update import map_update
import pygame


def map_generate(map):
    grass_img = pygame.image.load("img/grass.png")

    #   generate world

    #   capitol
    player_1 = map.players[0]
    player_2 = map.players[1]
    player_1.set_capitols(int((map.window_size_width-1)/4), int((map.window_size_height-1)/2), 1, map)
    player_2.set_capitols(int(map.window_size_width)-int((map.window_size_width-1)/4)-1, int((map.window_size_height-1)/2), 2, map)

    #       maly plus drzew kolo capitolu
    tree_core_x = player_1.capitol_X - 5
    tree_core_y = player_1.capitol_Y

    map.field_type[tree_core_x - 1][tree_core_y] = 'tr'
    map.field_type[tree_core_x + 1][tree_core_y] = 'tr'
    map.field_type[tree_core_x][tree_core_y] = 'tr'
    map.field_type[tree_core_x][tree_core_y - 1] = 'tr'
    map.field_type[tree_core_x][tree_core_y + 1] = 'tr'

    #   woda
    #   zmienna przechowujaca rozmiar morza
    water_size = 60
    #   sprawdz ktory rog wolny:
    water_core_x = 0
    water_core_y = 0
    corner = random.randint(0, 3)
    if map.field_type[int(map.window_size_width // 2 - 1)][0] == 'gr' and corner == 1:
        water_core_x = (map.window_size_width // 2 - 1)
    if map.field_type[0][map.window_size_height - 1] == 'gr' and corner == 2:
        water_core_y = map.window_size_height - 1
    if map.field_type[int(map.window_size_width // 2 - 1)][map.window_size_height - 1] == 'gr' and corner == 3:
        water_core_x = (map.window_size_width // 2 - 1)
        water_core_y = map.window_size_height - 1
    map.field_type[water_core_x][water_core_y] = 'wa'
    for i in range(water_size-1):
        water_core_x_tmp = water_core_x
        water_core_y_tmp = water_core_y
        while True:
            kierunek = random.randint(0, 3)
            if kierunek == 0:
                water_core_y_tmp -= 1
                if water_core_y_tmp < 0:
                    water_core_y_tmp = water_core_y
                    continue
            elif kierunek == 1:
                water_core_x_tmp += 1
                if water_core_x_tmp > (map.window_size_width // 2) - 1:
                    water_core_x_tmp = water_core_x
                    continue
            elif kierunek == 2:
                water_core_y_tmp += 1
                if water_core_y_tmp > map.window_size_height - 1:
                    water_core_y_tmp = water_core_y
                    continue
            elif kierunek == 3:
                water_core_x_tmp -= 1
                if water_core_x_tmp < 0:
                    water_core_x_tmp = water_core_x
                    continue

            if (map.field_type[water_core_x_tmp][water_core_y_tmp] == 'gr' and
                    map.field_owner[water_core_x_tmp][water_core_y_tmp] == 0):
                break
        map.field_type[water_core_x_tmp][water_core_y_tmp] = 'wa'

    #   mountains
    mountain_groups_count = 3
    mountain_groups_size = 10
    mountain_groups_size_difference = 3
    for i in range(mountain_groups_count):
        mountain_core_x = random.randint(0, int(map.window_size_width // 2) - 1)
        mountain_core_y = random.randint(0, int(map.window_size_height) - 1)
        while True:
            if (map.field_type[mountain_core_x][mountain_core_y] == 'gr'
                    and map.field_owner[mountain_core_x][mountain_core_y] == 0):
                break
            else:
                mountain_core_x = random.randint(0, int(map.window_size_width // 2) - 1)
                mountain_core_y = random.randint(0, int(map.window_size_height) - 1)
        map.field_type[mountain_core_x][mountain_core_y] = 'mo'
        
        for j in range(mountain_groups_size+(i * mountain_groups_size_difference)):
            mountain_core_x_tmp = mountain_core_x
            mountain_core_y_tmp = mountain_core_y
            while True:
                kierunek = random.randint(0, 3)
                if kierunek == 0:
                    mountain_core_y_tmp -= 1
                    if mountain_core_y_tmp < 0:
                        mountain_core_y_tmp = mountain_core_y
                        continue
                elif kierunek == 1:
                    mountain_core_x_tmp += 1
                    if mountain_core_x_tmp > (map.window_size_width // 2) - 1:
                        mountain_core_x_tmp = mountain_core_x
                        continue
                elif kierunek == 2:
                    mountain_core_y_tmp += 1
                    if mountain_core_y_tmp > map.window_size_height - 1:
                        mountain_core_y_tmp = mountain_core_y
                        continue
                elif kierunek == 3:
                    mountain_core_x_tmp -= 1
                    if mountain_core_x_tmp < 0:
                        mountain_core_x_tmp = mountain_core_x
                        continue

                if (map.field_type[mountain_core_x_tmp][mountain_core_y_tmp] == 'gr' and
                        map.field_owner[mountain_core_x_tmp][mountain_core_y_tmp] == 0):
                    break
            if j < (mountain_groups_size+(i * mountain_groups_size_difference)-i):
                map.field_type[mountain_core_x_tmp][mountain_core_y_tmp] = 'mo'
            else:
                map.field_type[mountain_core_x_tmp][mountain_core_y_tmp] = 'ir'

    #   generate trees
    #      wieksze grupy drzew
    #   ilosc grup drzew
    tree_groups_count = 4
    #   bazowy rozmiar ilosci drzew
    tree_grops_size = 15
    #   zmienna odpowiedzialna za przyrost ilosci drzew miedzy kolejnymi pojawiajacymi sie grupami
    tree_grops_extra_trees_cout = 5

    for i in range(tree_groups_count):
        while True:
            tree_core_x = random.randint(0, (map.window_size_width // 2) - 1)
            tree_core_y = random.randint(0, map.window_size_height - 1)
            if map.field_type[tree_core_x][tree_core_y] == 'gr' and map.field_owner[tree_core_x][tree_core_y] == 0:
                break
        map.field_type[tree_core_x][tree_core_y] = 'tr'
        for j in range((tree_grops_size-1)+(i * tree_grops_extra_trees_cout)):
            tree_core_x_tmp = tree_core_x
            tree_core_y_tmp = tree_core_y
            while True:
                kierunek = random.randint(0, 3)
                if kierunek == 0:
                    tree_core_y_tmp -= 1
                    if tree_core_y_tmp < 0:
                        tree_core_y_tmp = tree_core_y
                        continue
                elif kierunek == 1:
                    tree_core_x_tmp += 1
                    if tree_core_x_tmp > (map.window_size_width // 2) - 1:
                        tree_core_x_tmp = tree_core_x
                        continue
                elif kierunek == 2:
                    tree_core_y_tmp += 1
                    if tree_core_y_tmp > map.window_size_height-1:
                        tree_core_y_tmp = tree_core_y
                        continue
                elif kierunek == 3:
                    tree_core_x_tmp -= 1
                    if tree_core_x_tmp < 0:
                        tree_core_x_tmp = tree_core_x
                        continue

                if (map.field_type[tree_core_x_tmp][tree_core_y_tmp] == 'gr' and
                        map.field_owner[tree_core_x_tmp][tree_core_y_tmp] == 0):
                    break

            map.field_type[tree_core_x_tmp][tree_core_y_tmp] = 'tr'

    #   mirror map
    for j in range((int(map.window_size_height))):
        for i in range((int(map.window_size_width/2))):
            if map.field_type[i][j] == 'ca':
                continue
            map.field_type[map.window_size_width - i - 1][j] = map.field_type[i][j]

    map.turn = 1
    map.window = pygame.display.set_mode((map.window.get_width()+grass_img.get_width()*2, map.window.get_height()))

    map_update(map)
