from animation import *


class Character:
    def __init__(self, ani, x, y, speed, state, state_move, size_x, size_y):
        self.ani = ani
        self.x = x
        self.y = y
        self.speed = speed
        self.state = state
        self.state_move = state_move
        self.size_x = size_x
        self.size_y = size_y


mario = Character(small_mario_animation, 50, 50, 0, 'small', 'right_standing', 40, 40)
# goomba = pass
# koopagreen = pass
