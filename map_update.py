import pygame

grass_img = pygame.image.load("img/grass.png")

def highlight_borders(map, x, y):
    line_left = pygame.image.load("img/active_border/l_left.png")
    line_right = pygame.image.load("img/active_border/l_right.png")
    line_top = pygame.image.load("img/active_border/l_top.png")
    line_bottom = pygame.image.load("img/active_border/l_bottom.png")
    corner_left_top = pygame.image.load("img/active_border/c_lt.png")
    corner_left_bottom = pygame.image.load("img/active_border/c_lb.png")
    corner_right_top = pygame.image.load("img/active_border/c_rt.png")
    corner_right_bottom = pygame.image.load("img/active_border/c_rb.png")
    new_width = int(grass_img.get_width() * map.camera_zoom)
    if map.field_owner[x-1][y] != map.turn:
        scaled_hightlight = pygame.transform.scale(line_left, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x+1][y] != map.turn:
        scaled_hightlight = pygame.transform.scale(line_right, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x][y-1] != map.turn:
        scaled_hightlight = pygame.transform.scale(line_top, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x][y+1] != map.turn:
        scaled_hightlight = pygame.transform.scale(line_bottom, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x-1][y] == map.turn and map.field_owner[x][y-1] == map.turn and map.field_owner[x-1][y-1] != map.turn:
        scaled_hightlight = pygame.transform.scale(corner_left_top, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x+1][y] == map.turn and map.field_owner[x][y-1] == map.turn and map.field_owner[x+1][y-1] != map.turn:
        scaled_hightlight = pygame.transform.scale(corner_right_top, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x-1][y] == map.turn and map.field_owner[x][y+1] == map.turn and map.field_owner[x-1][y+1] != map.turn:
        scaled_hightlight = pygame.transform.scale(corner_left_bottom, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))
    if map.field_owner[x+1][y] == map.turn and map.field_owner[x][y+1] == map.turn and map.field_owner[x+1][y+1] != map.turn:
        scaled_hightlight = pygame.transform.scale(corner_right_bottom, (new_width, new_width))
        map.window.blit(scaled_hightlight, (x * new_width + map.camera_x * new_width,
                                            y * new_width + map.camera_y * new_width))

def show_number(map, number, top_position, left_position):
    number_img = None

    if number == 0:
        number_img = pygame.image.load("img/numbers/0.png")
    if number == 1:
        number_img = pygame.image.load("img/numbers/1.png")
    if number == 2:
        number_img = pygame.image.load("img/numbers/2.png")
    if number == 3:
        number_img = pygame.image.load("img/numbers/3.png")
    if number == 4:
        number_img = pygame.image.load("img/numbers/4.png")
    if number == 5:
        number_img = pygame.image.load("img/numbers/5.png")
    if number == 6:
        number_img = pygame.image.load("img/numbers/6.png")
    if number == 7:
        number_img = pygame.image.load("img/numbers/7.png")
    if number == 8:
        number_img = pygame.image.load("img/numbers/8.png")
    if number == 9:
        number_img = pygame.image.load("img/numbers/9.png")

    map.window.blit(number_img, (top_position, left_position))


def resource_number_display(map, number, left_position, top_position):

    margin_top = 39
    margin_left = 13

    if number > 99:
        show_number(map, number // 100, left_position + margin_left, top_position + margin_top,)
    left_position += margin_left
    if number > 9:
        show_number(map, (number % 100) // 10, left_position + margin_left, top_position + margin_top)
    left_position += margin_left
    show_number(map, number % 10, left_position + margin_left, top_position + margin_top)

def map_update(map):
    map.window.fill((0, 0, 0))
    #   img load
    tree_img = pygame.image.load("img/spruce.png")
    mountain_img = pygame.image.load("img/mountain.png")
    iron_ore_img = pygame.image.load("img/iron_ore.png")
    water_img = pygame.image.load("img/water.png")
    grid_img = pygame.image.load("img/empty.png")
    capitol_img = pygame.image.load("img/capitol.png")
    p1_field_img = pygame.image.load("img/p1_color.png")
    p2_field_img = pygame.image.load("img/p2_color.png")
    menu_img_p1 = pygame.image.load("img/invBackground_p1.png")
    menu_img_p2 = pygame.image.load("img/invBackground_p2.png")
    end_turn_img = pygame.image.load("img/end.png")
    resource_wood_img = pygame.image.load("img/wood.png")
    resource_stone_img = pygame.image.load("img/stone.png")
    resource_iron_img = pygame.image.load("img/iron.png")
    resource_pop_img = pygame.image.load("img/population.png")
    resource_research_img = pygame.image.load("img/research.png")
    menu_buildings_button_img = pygame.image.load("img/menu/buildings.png")
    menu_recrutation_button_img = pygame.image.load("img/menu/recrutation.png")
    menu_technology_button_img = pygame.image.load("img/menu/technology.png")
    menu_button_highlight = pygame.image.load("img/menu/button_highlight.png")

    for i in range(map.window_size_height):
        for j in range(map.window_size_width):
            #   grass

            new_width = int(grass_img.get_width() * map.camera_zoom)
            scaled_grass = pygame.transform.smoothscale(grass_img, (new_width, new_width))
            map.window.blit(scaled_grass, (j * new_width + map.camera_x * new_width,
                                           i * new_width + map.camera_y * new_width))

            #   water
            if map.field_type[j][i] == 'wa':
                scaled_water = pygame.transform.scale(water_img, (new_width, new_width))
                map.window.blit(scaled_water, (j * new_width + map.camera_x * new_width,
                                               i * new_width + map.camera_y * new_width))
            #   trees
            elif map.field_type[j][i] == 'tr':
                scaled_tree = pygame.transform.scale(tree_img, (new_width, new_width))
                map.window.blit(scaled_tree, (j * new_width + map.camera_x * new_width,
                                              i * new_width + map.camera_y * new_width))
            #   mountains
            elif map.field_type[j][i] == 'mo':
                scaled_mountain = pygame.transform.scale(mountain_img, (new_width, new_width))
                map.window.blit(scaled_mountain, (j * new_width + map.camera_x * new_width,
                                                  i * new_width + map.camera_y * new_width))
            #   iron ore
            elif map.field_type[j][i] == 'ir':
                scaled_iron = pygame.transform.scale(iron_ore_img, (new_width, new_width))
                map.window.blit(scaled_iron, (j * new_width + map.camera_x * new_width,
                                              i * new_width + map.camera_y * new_width))

    for i in range(map.window_size_height):
        for j in range(map.window_size_width):
            new_width = int(grass_img.get_width() * map.camera_zoom)
            #   player1
            if map.field_owner[j][i] == 1:
                scaled_field = pygame.transform.scale(p1_field_img, (new_width, new_width))
                map.window.blit(scaled_field, (j * new_width + map.camera_x * new_width,
                                               i * new_width + map.camera_y * new_width))
            #   player2
            elif map.field_owner[j][i] == 2:
                scaled_field = pygame.transform.scale(p2_field_img, (new_width, new_width))
                map.window.blit(scaled_field, (j * new_width + map.camera_x * new_width,
                                               i * new_width + map.camera_y * new_width))

            if map.field_type[j][i] == 'ca':
                scaled_capitol = pygame.transform.scale(capitol_img, (new_width, new_width))
                map.window.blit(scaled_capitol, (j * new_width + map.camera_x * new_width,
                                                 i * new_width + map.camera_y * new_width))

            scaled_grid = pygame.transform.scale(grid_img, (new_width, new_width))
            map.window.blit(scaled_grid, (j * new_width + map.camera_x * new_width,
                                          i * new_width + map.camera_y * new_width))
            if map.field_owner[j][i] == map.turn:
                highlight_borders(map, j, i)

    #   menu
    menu_top_position = 0
    if map.expand_left == 1:
        expand_left_1 = pygame.image.load("img/moves_1_1.png")
        menu_top_position += expand_left_1.get_height()/2
        map.window.blit(expand_left_1, (map.window.get_width()-expand_left_1.get_width(), menu_top_position))
    elif map.expand_left == 0:
        expand_left_0 = pygame.image.load("img/moves_0_1.png")
        menu_top_position += expand_left_0.get_height() / 2
        map.window.blit(expand_left_0, (map.window.get_width() - expand_left_0.get_width(), menu_top_position))
    #menu_top_position +=
    # if map.action == 1:
    #     action_img = pygame.image.load("img/movess_1_1.png")
    #     menu_top_position += expand_left_0.get_height() / 2
    #elif map.action == 0:
    arrow_turn = None
    if not map.menu_is_open:
        menu_top_position += (menu_top_position * 2) + (menu_top_position / 4)
        if map.turn == 1:
            map.window.blit(menu_img_p1, (map.window.get_width()-end_turn_img.get_width(), menu_top_position))
        elif map.turn == 2:
            map.window.blit(menu_img_p2, (map.window.get_width() - end_turn_img.get_width(), menu_top_position))
        map.menu_event_open = pygame.Rect(map.window.get_width() - end_turn_img.get_width(), menu_top_position,
                                          end_turn_img.get_width(), menu_img_p2.get_height())
        button_react = pygame.Rect(0, 0, 0, 0)
        for i in range(len(map.menu_button_hover)):
            if len(map.menu_button_hover) == i:
                map.menu_button_hover.append(button_react)
            else:
                map.menu_button_hover[i] = button_react


        menu_top_position += menu_img_p2.get_height()
    else:
        turn_img = None
        adjust_x = 50
        adjust_y = 24
        if map.turn == 1:
            turn_img = pygame.image.load("img/blueTurn.png")
        elif map.turn == 2:
            turn_img = pygame.image.load("img/reedTurn.png")

        menu_top_position += (menu_top_position * 2) + (menu_top_position / 4)
        menu_left_position = map.window.get_width() - menu_img_p2.get_width() + end_turn_img.get_width() / 2
        if map.turn == 1:
            map.window.blit(menu_img_p1, (menu_left_position, menu_top_position))
        elif map.turn == 2:
            map.window.blit(menu_img_p2, (menu_left_position, menu_top_position))
        map.menu_event_open = pygame.Rect(menu_left_position, menu_top_position,
                                          menu_img_p2.get_width(), menu_img_p2.get_height())

        map.window.blit(turn_img, (map.window.get_width() - menu_img_p2.get_width() + end_turn_img.get_width() / 2 +
                                   adjust_x, menu_top_position + menu_img_p2.get_height() - adjust_y))

        menu_top_position2 = menu_top_position + 130
        menu_left_position2 = menu_left_position + (menu_img_p2.get_width() - menu_buildings_button_img.get_width()) / 2

        #   resources in menu
        left_position = 70
        adjust_x = 9
        adjust_y = 50
        player = None

        if map.turn == 1:
            player = map.players[0]
        elif map.turn == 2:
            player = map.players[1]

        resource_wood = player.wood
        resource_iron = player.iron
        resource_stone = player.stone
        resource_pop = player.pop
        resource_research = player.research
        map.window.blit(resource_wood_img, (map.window.get_width() - menu_img_p2.get_width() + left_position,
                                            menu_top_position + adjust_y))
        resource_number_display(map, resource_wood, map.window.get_width() - menu_img_p2.get_width() + left_position,
                                menu_top_position + adjust_y)

        left_position += resource_wood_img.get_width() + adjust_x
        map.window.blit(resource_iron_img, (map.window.get_width() - menu_img_p2.get_width() + left_position,
                                            menu_top_position + adjust_y))
        resource_number_display(map, resource_iron, map.window.get_width() - menu_img_p2.get_width() + left_position,
                                menu_top_position + adjust_y)

        left_position += resource_wood_img.get_width() + adjust_x
        map.window.blit(resource_stone_img, (map.window.get_width() - menu_img_p2.get_width() + left_position,
                                             menu_top_position + adjust_y))
        resource_number_display(map, resource_stone, map.window.get_width() - menu_img_p2.get_width() + left_position,
                                menu_top_position + adjust_y)

        left_position += resource_wood_img.get_width() + adjust_x
        map.window.blit(resource_pop_img, (map.window.get_width() - menu_img_p2.get_width() + left_position,
                                           menu_top_position + adjust_y))
        resource_number_display(map, resource_pop, map.window.get_width() - menu_img_p2.get_width() + left_position,
                                menu_top_position + adjust_y)

        left_position += resource_wood_img.get_width() + adjust_x
        map.window.blit(resource_research_img, (map.window.get_width() - menu_img_p2.get_width() + left_position,
                                                menu_top_position + adjust_y))
        resource_number_display(map, resource_research,
                                map.window.get_width() - menu_img_p2.get_width() + left_position,
                                menu_top_position + adjust_y)

        if map.menu_submenu == 0:
            map.window.blit(menu_buildings_button_img, (menu_left_position2, menu_top_position2))
            button_react = pygame.Rect(menu_left_position2, menu_top_position2,
                                       menu_buildings_button_img.get_width(), menu_buildings_button_img.get_height())
            if len(map.menu_button_hover) == 0:
                map.menu_button_hover.append(button_react)
            else:
                map.menu_button_hover[0] = button_react

            menu_top_position3 = menu_top_position2 + menu_buildings_button_img.get_height() + 3*7
            map.window.blit(menu_recrutation_button_img, (menu_left_position2, menu_top_position3))
            button_react = pygame.Rect(menu_left_position2, menu_top_position3,
                                       menu_buildings_button_img.get_width(), menu_buildings_button_img.get_height())
            if len(map.menu_button_hover) == 1:
                map.menu_button_hover.append(button_react)
            else:
                map.menu_button_hover[1] = button_react

            menu_top_position4 = menu_top_position3 + menu_top_position3 - menu_top_position2
            map.window.blit(menu_technology_button_img, (menu_left_position2, menu_top_position4))
            button_react = pygame.Rect(menu_left_position2, menu_top_position4,
                                       menu_buildings_button_img.get_width(), menu_buildings_button_img.get_height())
            if len(map.menu_button_hover) == 2:
                map.menu_button_hover.append(button_react)
            else:
                map.menu_button_hover[2] = button_react

            if map.menu_button_highlighted[0]:
                map.window.blit(menu_button_highlight, (menu_left_position2, menu_top_position2))
            elif map.menu_button_highlighted[1]:
                map.window.blit(menu_button_highlight, (menu_left_position2, menu_top_position3))
            elif map.menu_button_highlighted[2]:
                map.window.blit(menu_button_highlight, (menu_left_position2, menu_top_position4))

            menu_top_position += menu_img_p2.get_height()

        elif map.menu_submenu == 1:
            # TODO poprawić podświetlenia guzików miedzy menu
            menu_buildings_dom = pygame.image.load("img/menu/budynki/dom.png")
            map.window.blit(menu_buildings_dom, (menu_left_position2, menu_top_position2))

    # if map.turn == 1:
    #     menu_top_position += (menu_top_position * 2) + (menu_top_position / 4)
    #     temp_menu_top = menu_top_position
    #     arrow_turn = pygame.image.load("img/p1_menuarrow.png")
    #     map.window.blit(arrow_turn, (map.window.get_width()-arrow_turn.get_width(), menu_top_position))
    #     menu_top_position += arrow_turn.get_height()
    # elif map.turn == 2:
    #     menu_top_position += (menu_top_position * 2) + (menu_top_position / 4)
    #     temp_menu_top = menu_top_position
    #     arrow_turn = pygame.image.load("img/p2_menuarrow.png")
    #     map.window.blit(arrow_turn, (map.window.get_width()-arrow_turn.get_width(), menu_top_position))
    #     menu_top_position += arrow_turn.get_height()
    x, y = map.menu_event_open.bottomleft
    menu_top_position = y + end_turn_img.get_height()/8
    map.window.blit(end_turn_img, (map.window.get_width()-end_turn_img.get_width(), menu_top_position))

    #   guziki
    map.end_turn_event = pygame.Rect(map.window.get_width()-end_turn_img.get_width(), menu_top_position,
                                     end_turn_img.get_width(), end_turn_img.get_height())


    pygame.display.update()
