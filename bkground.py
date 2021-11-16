from pico2d import *

class Bkground:
    def __init__(self):
        Bkground.image = load_image('resource/bg.png')
    def update(self):
        pass
    def draw(self, camera_x, camera_y):
        self.image.draw(400, 300, 800, 600)