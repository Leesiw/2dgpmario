from pico2d import *
# from character import *
from camera import *

class Map:
    image = None
    def __init__(self, width, height, tile_board, tile_x, tile_y):
        self.width = width
        self.height = height
        self.tile_board = tile_board
        self.tile_x = tile_x
        self.tile_y = tile_y

        self.tile_width = self.width // self.tile_x
        self.tile_height = self.height // self.tile_y

        if Map.image == None:
            Map.image = load_image('resource/tiles1.png')


def ground_collide(character, map): # 캐릭터와 바닥 충돌 체크
    # if character.y < 0:
    #     character.die = 'die'
    # else:
        x = int(character.x // map.tile_width)
        y = int((character.y - character.size_y // 2) // map.tile_height)

        # print(character.y, character.size_y)
        # print(y)

        if map.tile_board[x][y-1] == 3 or map.tile_board[x][y-1] == 4:
            y = y - 1
        if map.tile_board[x][y+1] == 3 or map.tile_board[x][y+1] == 4:
            y = y + 1

        if map.tile_board[x][y] == 0:
            if not character.jump_bool:
                # and (character.x + character.size_x / 2) % map.tile_width != 0
                character.jump_bool = True
                character.jump_power = 0
        elif map.tile_board[x][y] == 1: # flat ground
            if character.jump_bool and character.jump_power < 0:
                character.jump_bool = False
                character.y = y * map.tile_height + character.size_y // 2 + 10
        elif map.tile_board[x][y] == 3: # slopping ground right up
            if not character.jump_bool:
                character.y = (character.x % map.tile_width) / map.tile_width * map.tile_height + (y+1) * map.tile_height
                + character.size_y // 2 + 10
            elif character.jump_power < 0:
                character.jump_bool = False
                character.y = (character.x % map.tile_width) / map.tile_width * map.tile_height + (y+1) * map.tile_height
                + character.size_y // 2 + 10
        elif map.tile_board[x][y] == 4: # slopping ground right down
            if not character.jump_bool:
                character.y = map.tile_width - (character.x % map.tile_width) / map.tile_width * map.tile_height \
                              + (y-1) * map.tile_height + character.size_y // 2 + 10
            elif character.jump_power < 0:
                character.jump_bool = False
                character.y = map.tile_width - (character.x % map.tile_width) / map.tile_width * map.tile_height \
                              + (y-1) * map.tile_height + character.size_y // 2 + 10
        elif map.tile_board[x][y] == 2:
             character.y = y * map.tile_height + character.size_y // 2 + 10
             if character.jump_bool:
                 character.jump_bool = False



def init_test(map):
    map = Map(1600, 600, [[0] * 30 for _ in range(80)], 80, 30, {'goomba': 1, 'koopagreen': 1})
    map.tile_width = map.width // map.tile_x
    map.tile_height = map.height // map.tile_y

    for i in range(0, 39):
        map.tile_board[i][1] = 1
        map.tile_board[i][0] = 2

    for i in range(39, 55):
        map.tile_board[i][i - 37] = 3
        for j in range(0, i - 37):
            map.tile_board[i][j] = 2

    # map.all_goomba = [ Character('goomba', goomba_animation, 600, 50, 0, 'right', 'right_run', 50, 40, 600, 700, 'alive')]
    # map.all_koopagreen = [ Character('koopagreen', koopagreen_animation, 500, 50, 0, 'right', 'right_run', 25, 50, 500, 600, 'alive')]