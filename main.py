import sys

import pygame
from map_generate import map_generate
from map_update import map_update

pygame.init()

class Map:
    '''
    Field types:
        gr - grass
        ca - capitol
        tr - trees
        wa - water
        mo - mountains
        ir - iron
    '''
    field_type = []
    players = []
    field_owner = []
    grid_event = []
    window_size_width = 0
    window_size_height = 0
    number_of_players = 2
    window = pygame.display.set_mode((1280, 720))
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    turn = 1
    expand_left = 1
    action = 1
    end_turn_event = None
    menu_event_open = None
    menu_is_open = False
    menu_button_hover = []
    menu_button_highlighted = [False, False, False]
    camera_x = 0
    camera_y = 0
    camera_zoom = 1.0
    move_speed = 1.0
    map_width = 0
    map_height = 0

    def __init__(self):
        grid = pygame.image.load("img/empty.png")

        window_size_width_px = self.window.get_width() - self.window.get_width() % grid.get_width()
        self.window_size_width = int(window_size_width_px/grid.get_height())
        window_size_height_px = self.window.get_height() - self.window.get_height() % grid.get_height()
        self.window_size_height = int(window_size_height_px/grid.get_height())
        if self.window_size_width % 2 == 1:
            window_size_width_px += 25
            self.window_size_width += 1
        self.window = pygame.display.set_mode((window_size_width_px, window_size_height_px))

        self.map_width = self.window_size_width
        self.map_height = self.window_size_height

        #   Przygotowanie i zapelnienie tablicy o polach mapy
        for i in range(int(self.window_size_width)):
            tab = []
            tab2 = []
            tab3 = []
            for j in range(int(self.window_size_height)):
                tab.append('gr')
                tab2.append(0)
                tab3.append(pygame.Rect(i * grid.get_width(), j * grid.get_width(),
                                        grid.get_width(), grid.get_height()))
            self.field_type.append(tab)
            self.field_owner.append(tab2)
            self.grid_event.append(tab3)

        for i in range(self.number_of_players):
            self.add_player()

    def add_player(self):
        player = Player()
        self.players.append(player)


class Player:
    wood = 0
    iron = 222
    stone = 333
    pop = 444
    research = 555

    capitol_X = 0
    capitol_Y = 0

    def set_capitols(self, x, y, player_nr, map):
        water_img = pygame.image.load("img/water.png")
        map.window.blit(water_img, (x * water_img.get_width(), y * water_img.get_width()))
        self.capitol_x = x
        self.capitol_y = y
        map.field_type[x][y] = 'ca'
        #   Starting fields
        for i in range(3):
            for j in range(3):
                map.field_owner[x + 1 - i][y + 1 - j] = int(player_nr)

        pygame.display.update()

def end_turn(map):
    map.expand_left = 1
    map.turn += 1
    if map.turn > len(map.players):
        map.turn = 1
    map.window.fill((0, 0, 0))
    map_update(map)

def handle_zoom_event(map, event):
    mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
    grid = pygame.image.load("img/empty.png")

    width = int(grid.get_width() * map.camera_zoom)
    mouse_x_pixels = mouse_x_pos - mouse_x_pos % width
    mouse_y_pixels = mouse_y_pos - mouse_y_pos % width

    mouse_x = int(mouse_x_pixels / width)
    mouse_y = int(mouse_y_pixels / width)

    if event.button == 4:  # Scroll up
        map.camera_zoom += 0.1
    elif event.button == 5:  # Scroll down
        map.camera_zoom -= 0.1

    width = int(grid.get_width() * map.camera_zoom)

    mouse_x_pixels = mouse_x_pos - mouse_x_pos % width
    mouse_y_pixels = mouse_y_pos - mouse_y_pos % width

    new_mouse_x = int(mouse_x_pixels / width)
    new_mouse_y = int(mouse_y_pixels / width)
    map.camera_x = map.camera_x + new_mouse_x - mouse_x
    map.camera_y = map.camera_y + new_mouse_y - mouse_y

    map_update(map)
    new_scaled_grid_events(map)

def new_scaled_grid_events(map):
    grid = pygame.image.load("img/empty.png")
    new_width = int(grid.get_width() * map.camera_zoom)
    map.grid_event = []
    for i in range(int(map.map_width)):
        tab3 = []
        for j in range(int(map.map_height)):
            tab3.append(pygame.Rect(i * new_width + map.camera_x * new_width,
                                    j * new_width + map.camera_y * new_width, new_width, new_width))
        map.grid_event.append(tab3)

def main():
    run = True

    #   initialize game
    map = Map()
    map_generate(map)

    while run:
        pygame.time.Clock().tick(60)    # max 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # exit
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    end_turn(map)
                elif event.key == pygame.K_a:
                    map.camera_x += 1
                    map_update(map)
                    new_scaled_grid_events(map)
                elif event.key == pygame.K_d:
                    map.camera_x -= 1
                    map_update(map)
                    new_scaled_grid_events(map)
                elif event.key == pygame.K_w:
                    map.camera_y += 1
                    map_update(map)
                    new_scaled_grid_events(map)
                elif event.key == pygame.K_s:
                    map.camera_y -= 1
                    map_update(map)
                    new_scaled_grid_events(map)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()

                    if map.end_turn_event.collidepoint(mouse_pos):
                        end_turn(map)

                    #   Sprawdź, czy miejsce kliknięcia myszy koliduje z którymś z obszarów w grid_event
                    for i in range(len(map.grid_event)):
                        for j in range(len(map.grid_event[i])):
                            if map.grid_event[i][j].collidepoint(mouse_pos) and map.field_owner[i][j] == map.turn and \
                                    map.field_type[i][j] == 'tr':
                                map.field_type[i][j] = 'gr'
                                map.players[map.turn - 1].wood += 1

                            if (map.grid_event[i][j].collidepoint(mouse_pos) and map.expand_left > 0 and
                                    map.field_owner[i][j] == 0):
                                if (map.field_owner[i - 1][j] == map.turn or map.field_owner[i + 1][j] == map.turn or
                                        map.field_owner[i][j - 1] == map.turn or map.field_owner[i][j + 1] == map.turn):
                                    map.field_owner[i][j] = int(map.turn)
                                    map.expand_left -= 1

                    map_update(map)
                if event.button == 4:  # Scroll up
                    handle_zoom_event(map, event)
                elif event.button == 5:  # Scroll down
                    if map.camera_zoom >= 0.1:
                        handle_zoom_event(map, event)

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if map.menu_event_open.collidepoint(mouse_pos) and not map.menu_is_open:
                    map.menu_is_open = True

                    map_update(map)
                elif not map.menu_event_open.collidepoint(mouse_pos) and map.menu_is_open:
                    map.menu_is_open = False
                    map_update(map)

                if map.menu_is_open:
                    for i in range(len(map.menu_button_hover)):
                        if map.menu_button_hover[i].collidepoint(mouse_pos):
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                            map.menu_button_highlighted[i] = True
                            map_update(map)
                        elif map.menu_button_highlighted[i] == True:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            map.menu_button_highlighted[i] = False
                            map_update(map)

    pygame.quit()


if __name__ == "__main__":
    main()
