from pico2d import *
import game_framework

import server

class Ui:
    font = None
    Big_font = None
    def __init__(self):
        self.score = 0
        self.time = 100
        self.life_num = 3

        if Ui.font == None:
            Ui.font = load_font('resource/Super Mario Bros.ttf', 30)

        if Ui.Big_font == None:
            Ui.Big_font = load_font('resource/Super Mario Bros.ttf', 100)


    def draw(self, camera_x, camera_y):
        self.font.draw(0, 550, 'score : %d' % (self.score), (255, 255, 255))
        self.font.draw(0, 500, 'life : %d' % (self.life_num), (0, 0, 0))
        self.font.draw(600, 550, 'time : %d' % (self.time), (255, 255, 255))

        if server.stage.goal_in_bool:
            self.font.draw(400, 300, 'Stage Complete', (255, 255, 255))

    def update(self):
        self.time -= game_framework.frame_time