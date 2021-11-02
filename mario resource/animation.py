class Animation:
    def __init__(self, image_name, width, height, next, start_x, start_y, next_x_y, frame):
        self.image_name = image_name
        self.width = width
        self.height = height
        self.next = next
        self.start_x = start_x
        self.start_y = start_y
        self.next_x_y = next_x_y    # True면 x좌표 기준으로 next, False면 y좌표 기준으로 next
        self.frame = frame
        self.frame_now = 0



# mario
small_mario_animation = {}
small_mario_animation['left_standing'] = Animation('mario.png.gif', 20, 24, 20, 2, 215, True, 9)
small_mario_animation['right_standing'] = Animation('mario.png.gif', 20, 23, 20, 2, 192, True, 9)
small_mario_animation['left_jump'] = Animation('mario.png.gif', 20, 20, -20, 120, 114, True, 1)
small_mario_animation['right_jump'] = Animation('mario.png.gif', 18, 24, 20, 144, 114, True, 1)
small_mario_animation['left_run'] = Animation('mario.png.gif', 20, 24, 20, 3, 168, True, 12)
small_mario_animation['right_run'] = Animation('mario.png.gif', 20, 24, 20, 2, 143, True, 12)
small_mario_animation['die'] = Animation('mario.png.gif', 25, 24, 25, 56, 27, True, 4)

#goomba
goomba_animation = {}
goomba_animation['left_run'] = Animation('goomba_left.png', 30, 30, 31, 0, 867, False, 8)
goomba_animation['right_run'] = Animation('goomba_right.png', 30, 30, 31, 10, 867, False, 8)
goomba_animation['die'] = Animation('goomba_right.png', 30, 30, 31, 10, 604, False, 8)

#koopagreen
koopagreen_animation = {}
koopagreen_animation['left_run'] = Animation('koopagreen_left.gif', 16, 32, 32, 0, 1328, False, 16)
koopagreen_animation['right_run'] = Animation('koopagreen_right.gif', 16, 32, 32, 16, 1328, False, 16)
koopagreen_animation['die'] = Animation('koopagreen_right.gif', 0, 24, 20, 2, 604, False, 8)


