from camera import *
from map import *
from bkground import *
from character import *
from interaction import *
from box import *
from item import *
from ui import *
from fireball import *

class Stage:
    camera = None
    bk_ground = None
    id = None
    mario = None
    all_monster = None
    map = None
    all_box = None
    next_id = None
    all_item = None
    ui = None
    goal_in_x = None
    flag = None
    flag_image = None

    def __init__(self, id):
        self.camera = Camera(400, 300, 800, 600)
        self.bk_ground = Bkground()
        self.id = id

        if Stage.flag_image == None:
            Stage.flag_image = load_image('resource/flag.png')

        if id == 1: # 테스트용 맵
            self.mario = Mario(600, 50)
            all_goomba = All_goomba(2)
            all_goomba.list = [Goomba(20, 50, 100), Goomba(1700, 550, 1800), Goomba(1800, 550, 1900),
                               Goomba(1900, 550, 2000),
                               Goomba(3400, 450, 3600), Goomba(3500, 450, 3700), Goomba(3600, 450, 3800)]
            all_koopagreen = All_koopagreen(2)
            all_koopagreen.list = [# KoopaGreen(2050, 50, 2150), KoopaGreen(2100, 50, 2200),
                                   KoopaGreen(3000, 350, 3100), KoopaGreen(3100, 350, 3200),
                                   KoopaGreen(3200, 350,
                                              3300), ]  # , KoopaGreen(500, 50, 600)
            self.all_monster = All_monster(all_koopagreen, all_goomba, self.camera)
            self.map = Map(5000, 600, [[0] * 30 for _ in range(252)], 250, 30)
            self.all_box = All_box(3, self.camera)
            self.all_box.list = [Box(950, 250, None, None, 2), Box(1800, 400, None, None, 2), Box(1950, 400, None, None, 2), Box(2100, 100, None, None, 2),
                                 Box(4000, 350, None, None, 1), Box(4100, 350, None, None, 1), Box(4200, 350, None, None, 1), Box(4250, 450, None, None, 2)]
            self.all_box.list[0].item_que = [0]
            self.all_box.list[1].item_que = [0]
            self.all_box.list[2].item_que = [2]
            self.all_box.list[3].item_que = [1]
            self.all_box.list[7].item_que = [1]
            self.all_fireball = All_FireBall()
            self.next_id = 2
            self.all_item = ItemAll(self.camera)
            full_score = 30 * (len(all_goomba.list) + len(all_koopagreen.list))
            for b in self.all_box.list:
                for item in b.item_que:
                    if item == 0:
                        full_score += 50
                    elif item == 1:
                        full_score += 100
                    elif item == 2:
                        full_score += 70

            self.ui = Ui(full_score)
            self.goal_in_x = 4700
            self.goal_in_bool = False
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

            for i in range(58, 110):
                self.map.tile_board[i][0] = 1
            for i in range(65, 70):
                self.map.tile_board[i][2] = 1
                self.map.tile_board[i][1] = 2
                self.map.tile_board[i][0] = 2

            for i in range(70, 75):
                for j in range(0, 5):
                    self.map.tile_board[i][j] = 2
                self.map.tile_board[i][5] = 1

            for i in range(75, 80):
                for j in range(0, 8):
                    self.map.tile_board[i][j] = 2
                self.map.tile_board[i][8] = 1

            for i in range(80, 101):
                for j in range(0, 12):
                    self.map.tile_board[i][j] = 2
                self.map.tile_board[i][12] = 1

            for i in range(115, 250):
                self.map.tile_board[i][0] = 1

            for i in range(140, 150):
                self.map.tile_board[i][i - 139] = 3
                for j in range(0, i - 139):
                    self.map.tile_board[i][j] = 2
            for i in range(150, 155):
                self.map.tile_board[i][10] = 1
                for j in range(0, 10):
                    self.map.tile_board[i][j] = 2
            for i in range(155, 160):
                self.map.tile_board[i][-i + 165] = 4
                for j in range(0, -i + 165):
                    self.map.tile_board[i][j] = 2

            for i in range(160, 170):
                self.map.tile_board[i][5] = 1
                for j in range(0, 5):
                    self.map.tile_board[i][j] = 2

            for i in range(170, 180):
                self.map.tile_board[i][i - 164] = 3
                for j in range(0, i - 164):
                    self.map.tile_board[i][j] = 2
            for i in range(180, 185):
                self.map.tile_board[i][15] = 1
                for j in range(0, 15):
                    self.map.tile_board[i][j] = 2
            for i in range(185, 190):
                self.map.tile_board[i][-i + 200] = 4
                for j in range(0, -i + 200):
                    self.map.tile_board[i][j] = 2

            for i in range(190, 200):
                self.map.tile_board[i][10] = 1
                for j in range(0, 10):
                    self.map.tile_board[i][j] = 2

            for i in range(200, 210):
                self.map.tile_board[i][5] = 1
                for j in range(0, 5):
                    self.map.tile_board[i][j] = 2

            for i in range(210, 220):
                self.map.tile_board[i][1] = 1
                for j in range(0, 1):
                    self.map.tile_board[i][j] = 2

        elif id == 2:
            pass

    def draw(self, camera_x, camera_y):
        self.flag_image.draw(self.goal_in_x - camera_x, 130 - camera_y, 300, 300)

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
        if self.mario.x > self.goal_in_x:
            if not self.goal_in_bool:
                if self.ui.score >= self.ui.full_score:
                    self.all_box.list.append(Box(self.goal_in_x + 100, 130, None, None, 2))
                    num = len(self.all_box.list) - 1
                    self.all_box.list[num].item_que = [1]

                self.goal_in_bool = True
                self.goal_timer = time.time()

            if self.next_id != 0 and time.time() - self.goal_timer > 5.0:
                self.move_to_next(self.next_id)


        ground_collide(self.mario, self.map)
        for g in self.all_monster.goomba.list:
            ground_collide(g, self.map)
        for k in self.all_monster.koopagreen.list:
            ground_collide(k, self.map)
        for i in self.all_item.list:
            ground_collide(i, self.map)
        for f in self.all_fireball.list:
            ground_collide(f, self.map)

        for i in self.all_item.list:
            self.all_box.collide(i)

        if not self.goal_in_bool:
            for g in self.all_monster.goomba.list:
                if g.state == ALIVE:
                    if self.camera.start_x - g.size_x < g.x < self.camera.start_x + self.camera.width + g.size_x:
                        for f in self.all_fireball.list:
                            if fireball_with_monster(f, g):
                                self.all_fireball.list.remove(f)
            for k in self.all_monster.koopagreen.list:
                if k.state == ALIVE:
                    if self.camera.start_x - k.size_x < k.x < self.camera.start_x + self.camera.width + k.size_x:
                        for f in self.all_fireball.list:
                            if fireball_with_monster(f, k):
                                self.all_fireball.list.remove(f)

        # 마리오와 몬스터 상호작용
        if self.mario.unbeatable:
            if time.time() > self.mario.unbeatable_timer + 0.9:
                self.mario.unbeatable = False
                if self.mario.state == SMALL:
                    self.mario.size_y = 40

        else:
            if not self.goal_in_bool:
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





    def restart(self, id):

        if id == 1:  # 테스트용 맵
            self.mario.__init__(600, 50)
            all_goomba = All_goomba(2)
            all_goomba.list = [Goomba(20, 50, 100), Goomba(1700, 550, 1800), Goomba(1800, 550, 1900),
                               Goomba(1900, 550, 2000),
                               Goomba(3400, 450, 3600), Goomba(3500, 450, 3700), Goomba(3600, 450, 3800)]
            all_koopagreen = All_koopagreen(2)
            all_koopagreen.list = [#KoopaGreen(2050, 50, 2150), KoopaGreen(2100, 50, 2200),
                                   KoopaGreen(3000, 350, 3100), KoopaGreen(3100, 350, 3200),
                                   KoopaGreen(3200, 350,
                                              3300), ]  # , KoopaGreen(500, 50, 600)

            self.all_monster.__init__(all_koopagreen, all_goomba, self.camera)
            # self.map = Map(5000, 600, [[0] * 30 for _ in range(250)], 250, 30)
            self.all_box.__init__(3, self.camera)
            self.all_box.list = [Box(950, 250, None, None, 2), Box(1800, 400, None, None, 2),
                                 Box(1950, 400, None, None, 2), Box(2100, 100, None, None, 2),
                                 Box(4000, 350, None, None, 1), Box(4100, 350, None, None, 1),
                                 Box(4200, 350, None, None, 1), Box(4250, 450, None, None, 2)]
            self.all_box.list[0].item_que = [0]
            self.all_box.list[1].item_que = [0]
            self.all_box.list[2].item_que = [2]
            self.all_box.list[3].item_que = [1]
            self.all_box.list[7].item_que = [1]
            # self.next_id = 2
            self.all_fireball.__init__()
            self.all_item.__init__(self.camera)
            self.ui.life_num -= 1
            self.ui.time = 100
            self.ui.score = 0

        elif id == 2:
            self.mario.__init__(600, 50)
            all_goomba = All_goomba(2)
            all_goomba.list = [Goomba(20, 50, 100), Goomba(1700, 550, 1800), Goomba(1800, 550, 1900),
                               Goomba(1900, 550, 2000),
                               Goomba(3400, 450, 3600), Goomba(3500, 450, 3700), Goomba(3600, 450, 3800),
                               Goomba(2900, 350, 3000), Goomba(3000, 250, 3100),
                               Goomba(3100, 250, 3200),
                               ]

            all_koopagreen = All_koopagreen(2)
            all_koopagreen.list = [KoopaGreen(2050, 100, 2100), KoopaGreen(2100, 100, 2120),
                                   KoopaGreen(2900, 350, 3000), KoopaGreen(3000, 250, 3100),
                                   KoopaGreen(3100, 250, 3200),
                                   KoopaGreen(3200, 250,
                                              3300), ]  # , KoopaGreen(500, 50, 600)
            all_koopagreen.list = []  # , KoopaGreen(500, 50, 600)
            self.all_monster.__init__(all_koopagreen, all_goomba, self.camera)
            # self.map = Map(5000, 600, [[0] * 30 for _ in range(250)], 250, 30)
            self.all_box.__init__(3, self.camera)
            self.all_box.list = [Box(950, 250, None, None, 1), Box(1800, 400, None, None, 1),
                                 Box(1950, 400, None, None, 1), Box(2100, 200, None, None, 2),
                                 Box(4000, 350, None, None, 1), Box(4100, 350, None, None, 1),
                                 Box(4200, 350, None, None, 1), Box(4250, 450, None, None, 1),
                                 Box(50, 100, None, None, 2)]
            # self.all_box.list[0].item_que = [0]
            # self.all_box.list[1].item_que = [0]
            # self.all_box.list[2].item_que = [2]
            self.all_box.list[3].item_que = [1]
            self.all_box.list[8].item_que = [0]
            self.all_fireball = All_FireBall()
            # self.next_id = 2
            self.all_fireball.__init__()
            self.all_item.__init__(self.camera)
            self.ui.life_num -= 1
            self.ui.time = 100
            self.ui.score = 0

    def move_to_next(self, id):
        if id == 2:  # 테스트용 맵
            self.camera.__init__(400, 300, 800, 600)
            # self.bk_ground = Bkground()
            self.id = id

            if Stage.flag_image == None:
                Stage.flag_image = load_image('resource/flag.png')

            if id == 2:  # 테스트용 맵
                self.mario.__init__(600, 50)
                all_goomba = All_goomba(2)
                all_goomba.list = [Goomba(20, 50, 100), Goomba(1700, 550, 1800), Goomba(1800, 550, 1900),
                                   Goomba(1900, 550, 2000),
                                   Goomba(3400, 450, 3600), Goomba(3500, 450, 3700), Goomba(3600, 450, 3800),
                                   Goomba(2900, 350, 3000), Goomba(3000, 250, 3100),
                                   Goomba(3100, 250, 3200),
                                   ]

                all_koopagreen = All_koopagreen(2)
                all_koopagreen.list = [KoopaGreen(2050, 100, 2100), KoopaGreen(2100, 100, 2120),
                                       KoopaGreen(2900, 350, 3000), KoopaGreen(3000, 250, 3100),
                                       KoopaGreen(3100, 250, 3200),
                                       KoopaGreen(3200, 250,
                                                  3300), ]  # , KoopaGreen(500, 50, 600)
                all_koopagreen.list = []  # , KoopaGreen(500, 50, 600)
                self.all_monster.__init__(all_koopagreen, all_goomba, self.camera)
                self.map.__init__(5000, 600, [[0] * 30 for _ in range(252)], 250, 30)
                self.all_box.__init__(3, self.camera)
                self.all_box.list = [Box(950, 250, None, None, 1), Box(1800, 400, None, None, 1),
                                     Box(1950, 400, None, None, 1), Box(2100, 100, None, None, 2),
                                     Box(4000, 350, None, None, 1), Box(4100, 350, None, None, 1),
                                     Box(4200, 350, None, None, 1), Box(4250, 450, None, None, 1),
                                      Box(50, 100, None, None, 2)]
                # self.all_box.list[0].item_que = [0]
                # self.all_box.list[1].item_que = [0]
                # self.all_box.list[2].item_que = [2]
                self.all_box.list[3].item_que = [1]
                self.all_box.list[8].item_que = [0]
                self.all_fireball = All_FireBall()
                self.next_id = 0
                self.all_item.__init__(self.camera)
                full_score = 30 * (len(all_goomba.list) + len(all_koopagreen.list))
                for b in self.all_box.list:
                    for item in b.item_que:
                        if item == 0:
                            full_score += 50
                        elif item == 1:
                            full_score += 100
                        elif item == 2:
                            full_score += 70
                life = self.ui.life_num
                self.ui.__init__(full_score)
                self.ui.life_num = life
                self.goal_in_x = 4700
                self.goal_in_bool = False
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

                for i in range(58, 110):
                    self.map.tile_board[i][0] = 1
                for i in range(65, 70):
                    self.map.tile_board[i][2] = 1
                    self.map.tile_board[i][1] = 2
                    self.map.tile_board[i][0] = 2

                for i in range(70, 75):
                    for j in range(0, 5):
                        self.map.tile_board[i][j] = 2
                    self.map.tile_board[i][5] = 1

                for i in range(75, 80):
                    for j in range(0, 8):
                        self.map.tile_board[i][j] = 2
                    self.map.tile_board[i][8] = 1

                for i in range(80, 101):
                    for j in range(0, 12):
                        self.map.tile_board[i][j] = 2
                    self.map.tile_board[i][12] = 1

                for i in range(115, 250):
                    self.map.tile_board[i][0] = 1

                for i in range(140, 150):
                    self.map.tile_board[i][i - 139] = 3
                    for j in range(0, i - 139):
                        self.map.tile_board[i][j] = 2
                for i in range(150, 155):
                    self.map.tile_board[i][10] = 1
                    for j in range(0, 10):
                        self.map.tile_board[i][j] = 2
                for i in range(155, 160):
                    self.map.tile_board[i][-i + 165] = 4
                    for j in range(0, -i + 165):
                        self.map.tile_board[i][j] = 2

                for i in range(160, 170):
                    self.map.tile_board[i][5] = 1
                    for j in range(0, 5):
                        self.map.tile_board[i][j] = 2

                for i in range(170, 180):
                    self.map.tile_board[i][i - 164] = 3
                    for j in range(0, i - 164):
                        self.map.tile_board[i][j] = 2
                for i in range(180, 185):
                    self.map.tile_board[i][15] = 1
                    for j in range(0, 15):
                        self.map.tile_board[i][j] = 2
                for i in range(185, 190):
                    self.map.tile_board[i][-i + 200] = 4
                    for j in range(0, -i + 200):
                        self.map.tile_board[i][j] = 2

                for i in range(190, 200):
                    self.map.tile_board[i][10] = 1
                    for j in range(0, 10):
                        self.map.tile_board[i][j] = 2

                for i in range(200, 210):
                    self.map.tile_board[i][5] = 1
                    for j in range(0, 5):
                        self.map.tile_board[i][j] = 2

                for i in range(210, 220):
                    self.map.tile_board[i][1] = 1
                    for j in range(0, 1):
                        self.map.tile_board[i][j] = 2





