from koopagreen import *
from goomba import *

class All_monster:
    def __init__(self, koopagreen, goomba, camera):
        self.koopagreen = koopagreen
        self.goomba = goomba
        self.camera = camera

    def draw(self):
        # print(self.camera.start_x, self.camera.x)
        for g in self.goomba.list:
            if self.camera.start_x - g.size_x < g.x < self.camera.start_x + self.camera.width + g.size_x:
                g.draw(self.camera.start_x, self.camera.start_y)
        for k in self.koopagreen.list:
            if self.camera.start_x - k.size_x < k.x < self.camera.start_x + self.camera.width + k.size_x:
                k.draw(self.camera.start_x, self.camera.start_y)

    def update(self):
        self.goomba.update()
        self.koopagreen.update()