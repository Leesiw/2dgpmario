from camera import *
from map import *
from bkground import *
from character import *
from interaction import *
from box import *
from item import *

class Stage:
    def __init__(self, id):
        self.camera = Camera(400, 300, 800, 600)
        self.bk_ground = Bkground()

        if id == 1: # 테스트용 맵
            self.mario = Mario(600, 50)
            all_goomba = All_goomba(2)
            all_goomba.list = [Goomba(200, 50, 300)]
            all_koopagreen = All_koopagreen(2)
            all_koopagreen.list = [KoopaGreen(400, 50, 500), KoopaGreen(500, 50, 600)]
            self.all_monster = All_monster(all_koopagreen, all_goomba, self.camera)
            self.map = Map(5000, 600, [[0] * 30 for _ in range(250)], 250, 30)
            self.all_box = All_box(3, self.camera)
            self.all_box.list = [Box(950, 250, None, None, 2)]
            self.all_box.list[0].item_que = [2, 0]
            self.next_id = 2
            self.all_item = ItemAll(self.camera)

            for i in range(0, 39):
                self.map.tile_board[i][1] = 1
                self.map.tile_board[i][0] = 2

            for i in range(39, 45):
                self.map.tile_board[i][i - 37] = 3
                for j in range(0, i - 37):
                    self.map.tile_board[i][j] = 2
            for i in range(45, 51):
                self.map.tile_board[i][7] = 1
                for j in range(0, 7):
                    self.map.tile_board[i][j] = 2

            for i in range(51, 58):
                self.map.tile_board[i][-i + 58] = 4
                for j in range(0, -i + 58):
                    self.map.tile_board[i][j] = 2
            for i in range(58, 150):
                self.map.tile_board[i][0] = 1
            for i in range(65, 70):
                self.map.tile_board[i][2] = 1
                self.map.tile_board[i][1] = 2
                self.map.tile_board[i][0] = 2

            for i in range(71, 75):
                self.map.tile_board[i][5] = 1

            for i in range(76, 80):
                self.map.tile_board[i][8] = 1

            for i in range(81, 85):
                self.map.tile_board[i][15] = 1

        elif id == 2:
            pass

    def draw(self, camera_x, camera_y):
        x_first = self.camera.x - (self.camera.width / 2)  # // map.tile_width - 1
        y_first = self.camera.y - (self.camera.height / 2)  # // map.tile_height - 2

        x_tile_first = int(x_first // self.map.tile_width)
        x_tile_last = int(x_tile_first + (self.camera.width // self.map.tile_width) + 2)
        y_tile_first = int(y_first // self.map.tile_height)
        y_tile_last = int(y_tile_first + (self.camera.height // self.map.tile_height))

        for i in range(x_tile_first, x_tile_last):
            for j in range(y_tile_first, y_tile_last):
                if self.map.tile_board[i][j] == 1:  # grass
                    self.map.image.clip_draw(2, 1282, 90, 30, i * self.map.tile_width - x_first, j * self.map.tile_height - y_first, self.map.tile_width, self.map.tile_height)
                elif self.map.tile_board[i][j] == 2:  # earth
                    self.map.image.clip_draw(2, 1265, 90, 30, i * self.map.tile_width - x_first, j * self.map.tile_height - y_first, self.map.tile_width, self.map.tile_height)
                elif self.map.tile_board[i][j] == 3:  # slopping ground right up
                    self.map.image.clip_draw(0, 0, 81, 71, i * self.map.tile_width - x_first, j * self.map.tile_height - y_first, self.map.tile_width, self.map.tile_height)
                elif self.map.tile_board[i][j] == 4:  # slopping ground right up
                    self.map.image.clip_draw(81, 0, 81, 71, i * self.map.tile_width - x_first, j * self.map.tile_height - y_first, self.map.tile_width, self.map.tile_height)

    def update(self):
        update_camera(self.camera, self.map, self.mario)
        # 카메라 업데이트

        ground_collide(self.mario, self.map)
        for g in self.all_monster.goomba.list:
             ground_collide(g, self.map)
        for k in self.all_monster.koopagreen.list:
            ground_collide(k, self.map)
        for i in self.all_item.list:
            ground_collide(i, self.map)
        for f in self.mario.all_fireball.list:
            ground_collide(f, self.map)


        character_camera_update(self.mario, self.camera)
        self.all_monster.camera = self.camera

        self.all_box.collide(self.mario)
        for i in self.all_item.list:
            self.all_box.collide(i)

        for g in self.all_monster.goomba.list:
            if g.state == ALIVE:
                if self.camera.start_x - g.size_x < g.x < self.camera.start_x + self.camera.width + g.size_x:
                    for f in self.mario.all_fireball.list:
                        if fireball_with_monster(f, g):
                            self.mario.all_fireball.list.remove(f)
        for k in self.all_monster.koopagreen.list:
            if k.state == ALIVE:
                if self.camera.start_x - k.size_x < k.x < self.camera.start_x + self.camera.width + k.size_x:
                    for f in self.mario.all_fireball.list:
                        if fireball_with_monster(f, k):
                            self.mario.all_fireball.list.remove(f)

        # 마리오와 몬스터 상호작용
        if self.mario.unbeatable:
            if time.time() > self.mario.unbeatable_timer + 3.0:
                self.mario.unbeatable = False
        else:
            for g in self.all_monster.goomba.list:
                if g.state == ALIVE:
                    if self.camera.start_x - g.size_x < g.x < self.camera.start_x + self.camera.width + g.size_x:
                        mario_with_monster(self.mario, g)
                        mario_with_goomba(self.mario, g)
            for k in self.all_monster.koopagreen.list:
                if k.state == ALIVE:
                    if self.camera.start_x - k.size_x < k.x < self.camera.start_x + self.camera.width + k.size_x:
                        mario_with_monster(self.mario, k)


        for i in self.all_item.list:
            if self.camera.start_x - i.size_x < i.x < self.camera.start_x + self.camera.width + i.size_x:
                if mario_with_item(self.mario, i):
                    self.all_item.list.remove(i)



