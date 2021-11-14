from pico2d import *

class Coin:
    pass

class RedMushroom:
    image = load_image('resource/mushroom.png')
    speed = (12.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
    def enter(item, event):
        pass

    def exit(item, event):
        pass

    def do(item):
        item.x += item.dir * RedMushroom.speed *

    def draw(block, camera_x, camera_y):
        RedMushroom.image.draw()


class GreenMushroom:
    image = load_image('resource/greenmushroom.png')
    speed = (10.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25

    def enter(item, event):
        pass

    def exit(item, event):
        pass

    def do(item):
        item.x += item.dir * GreenMushroom.speed

    def draw(block, camera_x, camera_y):
        GreenMushroom.image.draw()

class Flower:
    image = load_image('resource/fireflower.png')

    def enter(item, event):
        pass

    def exit(item, event):
        pass

    def do(item):
        pass

    def draw(block, camera_x, camera_y):
        GreenMushroom.image.draw()

class Item:
    width, height = 25, 25
    def __init__(self, type, x, y, direction):
        self.type = type
        self.x = x
        self.y = y
        self.direction = direction
    def draw(self):
        self.cur_state.draw(self)


class ItemAll:
    def __init__(self, camera):
        self.list = []
        self.camera = camera
    def draw(self):
        for i in self.list:
            i.draw(self.camera.start_x, self.camera.start_y)

    def update(self):
        self.goomba.update()
        self.koopagreen.update()