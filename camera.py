from map import *
import server

class Camera:
    def __init__(self, x, y, width, height, start_x=0, start_y=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start_x = 0
        self.start_y = 0
    def update(self):
        if server.stage.mario.x < self.width / 2:
            self.x = self.width / 2
            self.start_x = 0
        elif server.stage.mario.x >= server.stage.map.width - (self.width / 2):
            self.x = server.stage.map.width - (self.width / 2) - server.stage.map.tile_width
            self.start_x = self.x - (self.width / 2)
        else:
            self.x = server.stage.mario.x
            self.start_x = self.x - (self.width / 2)

        if server.stage.mario.y < self.height / 2:
            self.y = self.height / 2
            self.start_y = 0
        elif server.stage.mario.y > self.height - (self.height / 2):
            self.y = self.height - (self.height / 2)
            self.start_y = self.y - (self.height / 2)
        else:
            self.y = server.stage.mario.y
            self.start_y = self.y - (self.height / 2)
    def draw(self, camera_x, camera_y):
        pass


def update_camera(camera, map, mario):
    if mario.x < camera.width / 2:
        camera.x = camera.width / 2
        camera.start_x = 0
    elif mario.x > map.width - (camera.width / 2):
        camera.x = map.width - (camera.width / 2)
        camera.start_x = camera.x - (camera.width / 2)
    else:
        camera.x = mario.x
        camera.start_x = camera.x - (camera.width / 2)

    if mario.y < camera.height / 2:
        camera.y = camera.height / 2
        camera.start_y = 0
    elif mario.y > camera.height - (camera.height / 2):
        camera.y = camera.height - (camera.height / 2)
        camera.start_y = camera.y - (camera.height / 2)
    else:
        camera.y = mario.y
        camera.start_y = camera.y - (camera.height / 2)

def draw_map(map, camera):
    x_first = camera.x - (camera.width / 2) # // map.tile_width - 1
    y_first = camera.y - (camera.height / 2) # // map.tile_height - 2

    x_tile_first = int(x_first // 20); x_tile_last = int(x_tile_first + (camera.width // 20) + 2)
    y_tile_first = int(y_first // 20); y_tile_last = int(y_tile_first + (camera.height // 20))
    # if x_tile_first < 0:
    #      x_tile_first = 0
    # if y_tile_first < 0:
    #      y_tile_first = 0
    # if x_tile_last > map.tile_x:
    #      x_tile_last = map.tile_x
    # if y_tile_last > map.tile_y:
    #      y_tile_last = map.tile_y

    tile = load_image('tiles1.png')

    for i in range(x_tile_first, x_tile_last):
        for j in range(y_tile_first, y_tile_last):
            if map.tile_board[i][j] == 1:   # grass
                tile.clip_draw(2, 1282, 90, 30, i * 20 - x_first, j * 20 - y_first, 20, 20)
            elif map.tile_board[i][j] == 2:   # earth
                tile.clip_draw(2, 1265, 90, 30, i * 20 - x_first, j * 20 - y_first, 20, 20)
            elif map.tile_board[i][j] == 3: # slopping ground right up
                tile.clip_draw(0, 0, 81, 71, i * 20 - x_first, j * 20 - y_first, 20, 20)
            elif map.tile_board[i][j] == 4: # slopping ground right up
                tile.clip_draw(81, 0, 81, 71, i * 20 - x_first, j * 20 - y_first, 20, 20)

def character_camera_update(character, camera):
    character.camera_x, character.camera_y = camera.start_x, camera.start_y