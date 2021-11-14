from pico2d import *
import game_framework

class QmarkState:
    def enter(block, event):
        pass

    def exit(block, event):
        pass

    def do(block):
        block.frame = (block.frame + block.action_speed * game_framework.frame_time) % 4

    def draw(block, camera_x, camera_y):
        block.image.clip_draw(290 + 17 * int(block.frame), 138, 16, 16, block.x - camera_x, block.y - camera_y, block.width, block.height)

class CommonState:
    def enter(block, event):
        pass

    def exit(block, event):
        pass

    def do(block):
        block.frame = (block.frame + block.action_speed * game_framework.frame_time) % 4

    def draw(block, camera_x, camera_y):
        pass
        block.image.clip_draw(290 + 17 * int(block.frame), 121, 16, 16, block.x - camera_x, block.y - camera_y, block.width, block.height)

class UsedState:
    def enter(block, event):
        pass

    def exit(block, event):
        pass

    def do(block):
        pass

    def draw(block, camera_x, camera_y):
        block.image.clip_draw(358, 138, 16, 16, block.x - camera_x, block.y - camera_y, block.width, block.height)

class Box:
    width = 25
    height = 25
    image = None
    def __init__(self, x, y, item, coin_number, state):
        self.x = x
        self.y = y
        self.state = state
        self.item = item
        self.coin_number = coin_number
        self.action_speed = 1.0 / 0.1
        self.frame = 0

        self.left = self.x - self.width / 2
        self.right = self.x + self.width / 2
        self.top = self.y + self.height / 2
        self.bottom = self.y - self.height / 2

        if state == 0:
            self.cur_state = UsedState
        elif state == 1:
            self.cur_state = CommonState
        elif state == 2:
            self.cur_state = QmarkState
        self.cur_state.enter(self, None)
        if Box.image == None:
            Box.image = load_image('resource/tiles.png')
    def update(self):
        self.cur_state.do(self)

    def draw(self, camera_x, camera_y):
        self.cur_state.draw(self, camera_x, camera_y)
    def collide(self, character, on_box):
        c_left = character.x - character.size_x / 2
        c_bottom = character.y - character.size_y / 2
        c_right = character.x + character.size_x / 2
        c_top = character.y + character.size_y / 2

        if self.left < c_right and c_left < self.right:
            if self.bottom < c_top < self.top:  # 블록 두드렸을 때
                character.y = self.bottom - character.size_y / 2
                character.jump_power = 0.0
            if self.bottom <= c_bottom <= self.top: # 블록 위에 섰을 때
                character.y = self.top + character.size_y / 2
                character.jump_bool = False
                on_box = True

        if self.bottom < c_top and c_bottom < self.top:
            if self.left < c_right < self.right:
                character.x = self.left - character.size_x / 2
            if self.left < c_left < self.right: # 블록 위에 섰을 때
                character.x = self.right + character.size_x / 2




class All_box:
    def __init__(self, num, camera):
        self.num = num
        self.list = []
        self.camera = camera

    def draw(self):
        # print(self.camera.start_x, self.camera.x)
        for b in self.list:
            if self.camera.start_x - b.width < b.x < self.camera.start_x + self.camera.width + b.width:
                b.draw(self.camera.start_x, self.camera.start_y)

    def update(self):
        for b in self.list:
            b.update()

    def collide(self, character):
        on_box = False
        for b in self.list:
            if character.x - character.size_x / 2 < b.right and character.x + character.size_x / 2 > b.left:
                b.collide(character, on_box)
        character.on_box = on_box