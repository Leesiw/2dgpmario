from camera import *
from map import *
from bkground import *
from character import *

class Stage:
    def __init__(self, id):
        self.camera = Camera(400, 300, 800, 600)
        self.bk_ground = Bkground()

        if id == 1: # 테스트용 맵
            self.mario = Mario(600, 50)
            self.all_goomba = All_goomba(3)
            self.all_goomba.list = [Goomba(100, 50, 200), Goomba(200, 50, 300), Goomba(300, 50, 400)]
            self.all_koopagreen = All_koopagreen(3)
            self.all_koopagreen.list = [KoopaGreen(400, 50, 500), KoopaGreen(500, 50, 600), KoopaGreen(600, 50, 700)]
            self.map = Map(1600, 600, [[0] * 30 for _ in range(80)], 80, 30)

            for i in range(0, 39):
                self.map.tile_board[i][1] = 1
                self.map.tile_board[i][0] = 2

            for i in range(39, 55):
                self.map.tile_board[i][i - 37] = 3
                for j in range(0, i - 37):
                    self.map.tile_board[i][j] = 2

        elif id == 2:
            pass

    def draw(self):
        x_first = self.camera.x - (self.camera.width / 2)  # // map.tile_width - 1
        y_first = self.camera.y - (self.camera.height / 2)  # // map.tile_height - 2

        x_tile_first = int(x_first // 20);
        x_tile_last = int(x_tile_first + (self.camera.width // 20) + 2)
        y_tile_first = int(y_first // 20);
        y_tile_last = int(y_tile_first + (self.camera.height // 20))

        for i in range(x_tile_first, x_tile_last):
            for j in range(y_tile_first, y_tile_last):
                if self.map.tile_board[i][j] == 1:  # grass
                    self.map.image.clip_draw(2, 1282, 90, 30, i * 20 - x_first, j * 20 - y_first, 20, 20)
                elif self.map.tile_board[i][j] == 2:  # earth
                    self.map.image.clip_draw(2, 1265, 90, 30, i * 20 - x_first, j * 20 - y_first, 20, 20)
                elif self.map.tile_board[i][j] == 3:  # slopping ground right up
                    self.map.image.clip_draw(0, 0, 81, 71, i * 20 - x_first, j * 20 - y_first, 20, 20)
                elif self.map.tile_board[i][j] == 4:  # slopping ground right up
                    self.map.image.clip_draw(81, 0, 81, 71, i * 20 - x_first, j * 20 - y_first, 20, 20)

    def update(self):
        update_camera(self.camera, self.map, self.mario)

        ground_collide(self.mario, self.map)
        for g in self.all_goomba.list:
            ground_collide(g, self.map)
        for k in self.all_koopagreen.list:
            ground_collide(k, self.map)

        character_camera_update(self.mario, self.camera)
        for g in self.all_goomba.list:
            character_camera_update(g, self.camera)
        for k in self.all_koopagreen.list:
            character_camera_update(k, self.camera)


