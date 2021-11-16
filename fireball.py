from pico2d import *
import game_framework

class FireBall:
    image = None
    name = 'fire_ball'
    speed = (30.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
    g = 5 * (35.3094 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
    jump_power_first = (30.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25

    def __init__(self, x, y, dir):
        FireBall.image = load_image('resource/fireball.png')
        self.x = x
        self.y = y
        self.dir = dir
        self.jump_power = self.jump_power_first
        self.jump_bool = True
        self.size_x, self.size_y = 20, 20
        self.bound_num = 0
    def do(self):
        self.x += self.dir * self.speed * game_framework.frame_time
        if self.jump_bool:
            self.jump_power -= self.g * game_framework.frame_time
            self.y += self.jump_power * game_framework.frame_time
        else:
            self.jump_power = self.jump_power_first
            self.bound_num += 1
            if self.bound_num > 2:
                return True
            self.jump_bool = True
        return False
    def draw(self, camera_x, camera_y):
        self.image.draw(self.x - camera_x + self.size_x / 2, self.y - camera_y, 20, 20)


class All_FireBall:
    def __init__(self):
        self.list = []

    def update(self):
        for f in self.list:
            if f.do():
                self.list.remove(f)

    def draw(self, camera_x, camera_y):
        for f in self.list:
            f.draw(camera_x, camera_y)



