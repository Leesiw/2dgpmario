from pico2d import *

class Map:
    def __init__(self, width, height, tile_board, tile_x, tile_y, tile_name):
        self.width = width
        self.height = height
        self.tile_board = tile_board
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.tile_name = tile_name


test_map = Map(800, 600, [[0] * 30 for _ in range(40)], 40, 30, 'tiles1.png')
for i in range(0, 39):
    test_map.tile_board[i][1] = 1


def draw_map(map, tile_name):
    tile = load_image(tile_name)
    for j in range(0, map.tile_x):
        for k in range(0, map.tile_y):
            if map.tile_board[j][k] == 1:
                tile.clip_draw(2, 1282, 90, 30, j * 20, k * 20, 20, 20)


