class Animation:
    def __init__(self, image_name, width, height, next, start_x, start_y, frame, frame_now):
        self.image_name = image_name
        self.width = width
        self.height = height
        self.next = next
        self.start_x = start_x
        self.start_y = start_y
        self.frame = frame
        self.frame_now = frame_now


# mario
small_mario_animation = {}
small_mario_animation['left_standing'] = Animation('mario.png.gif', 20, 24, 20, 2, 216, 9, 0)
small_mario_animation['right_standing'] = Animation('mario.png.gif', 20, 24, 20, 2, 191, 9, 0)
small_mario_animation['left_jump'] = Animation('mario.png.gif', 20, 20, -20, 120, 115, 7, 0)
small_mario_animation['right_jump'] = Animation('mario.png.gif', 18, 24, 20, 144, 115, 7, 0)
small_mario_animation['left_run'] = Animation('mario.png.gif', 20, 24, 20, 3, 168, 12, 0)
small_mario_animation['right_run'] = Animation('mario.png.gif', 20, 24, 20, 2, 143, 12, 0)