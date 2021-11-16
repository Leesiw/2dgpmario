from pico2d import *
import game_framework

class Coin:
    pass

class RedMushroom:

    speed = (12.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
    def enter(item, event):
        pass

    def exit(item, event):
        pass

    def do(item):
        item.x += item.dir * RedMushroom.speed * game_framework.frame_time

    def draw(item, camera_x, camera_y):
        item.rm_image.draw(item.x -camera_x, item.y - camera_y, 25, 25)


class GreenMushroom:
    speed = (10.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25

    def enter(item, event):
        pass

    def exit(item, event):
        pass

    def do(item):
        item.x += item.dir * GreenMushroom.speed * game_framework.frame_time

    def draw(item, camera_x, camera_y):
        item.gm_image.draw(item.x -camera_x, item.y - camera_y, 25, 25)

class Flower:


    def enter(item, event):
        pass

    def exit(item, event):
        pass

    def do(item):
        pass

    def draw(item, camera_x, camera_y):
        item.ff_image.draw(item.x -camera_x, item.y - camera_y, 25, 25)

class Item:

    rm_image = None
    gm_image = None
    ff_image = None
    name = 'item'
    g = (35.3094 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25

    width, height = 25, 25
    def __init__(self, type, x, y, direction):
        self.type = type
        self.x = x
        self.y = y
        self.size_x = 25
        self.size_y = 25
        self.jump_bool = False
        self.on_box = False
        self.start_y = y
        self.dir = direction
        self.type = type

        if type == 0:
            self.cur_state = RedMushroom
        elif type == 1:
            self.cur_state = GreenMushroom
        elif type == 2:
            self.cur_state = Flower

        if Item.rm_image == None:
            Item.rm_image = load_image('resource/mushroom.png')
        if Item.gm_image == None:
            Item.gm_image = load_image('resource/greenmushroom.png')
        if Item.ff_image == None:
            Item.ff_image = load_image('resource/fireflower.png')
    def update(self):
        if self.jump_bool:
            current_time = game_framework.time.time() - self.time
            self.jump_power -= self.g * current_time
            self.y += self.jump_power * game_framework.frame_time
        self.cur_state.do(self)

    def draw(self, camera_x, camera_y):
        self.cur_state.draw(self, camera_x, camera_y)


class ItemAll:
    def __init__(self, camera):
        self.list = []
        self.camera = camera
    def draw(self, camera_x, camera_y):
        for i in self.list:
            i.draw(self.camera.start_x, self.camera.start_y)

    def update(self):
        for i in self.list:
            i.update()