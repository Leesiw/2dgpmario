from koopagreen import *
from goomba import *

class All_monster:
    def __init__(self, koopagreen, goomba, camera):
        self.koopagreen = koopagreen
        self.goomba = goomba
        self.camera = camera

    def draw(self, camera_x, camera_y):
        # print(self.camera.start_x, self.camera.x)
        for g in self.goomba.list:
            if camera_x - g.size_x < g.x < camera_x + self.camera.width + g.size_x:
                g.draw(camera_x, camera_y)
        for k in self.koopagreen.list:
            if camera_x - k.size_x < k.x < camera_x + self.camera.width + k.size_x:
                k.draw(camera_x, camera_y)

    def update(self):
        self.goomba.update()
        self.koopagreen.update()