# from animation import *
# from camera import *
# from map import *
from pico2d import *

history = []

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, DEBUG_KEY = range(6)

event_name = ['RIGHT_DOWN', 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_d) : DEBUG_KEY,

    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class IdleState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += 1
        elif event == LEFT_DOWN:
            mario.velocity -= 1
        elif event == RIGHT_UP:
            mario.velocity -= 1
        elif event == LEFT_UP:
            mario.velocity += 1

    def exit(mario, event):
        if event == SPACE:
            mario.jump_start()

    def do(mario):
        mario.frame = (mario.frame + 1) % 9

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(2 + mario.frame * 20, 192, 20, 23, mario.x - mario.camera_x, mario.y - mario.camera_y, 40, 40)
        else:
            mario.image.clip_draw(2 + mario.frame * 20, 215, 18, 24, mario.x - mario.camera_x, mario.y - mario.camera_y, 40, 40)

class RunState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += 1
        elif event == LEFT_DOWN:
            mario.velocity -= 1
        elif event == RIGHT_UP:
            mario.velocity -= 1
        elif event == LEFT_UP:
            mario.velocity += 1
        mario.dir = mario.velocity

    def exit(mario, event):
        mario.speed = 0
        if event == SPACE:
            mario.jump_start()

    def do(mario):
        mario.frame = (mario.frame + 1) % 12

        if mario.speed < 5:
            mario.speed += 0.5
        mario.x += mario.velocity * mario.speed
        mario.x = clamp(25, mario.x, 1600 - 25)

    def draw(mario):
        if mario.velocity == 1:
            mario.image.clip_draw(2 + mario.frame * 20, 143, 20, 24, mario.x - mario.camera_x, mario.y - mario.camera_y, 40, 40)
        else:
            mario.image.clip_draw(3 + mario.frame * 20, 168, 20, 24, mario.x - mario.camera_x, mario.y - mario.camera_y, 40, 40)



next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState}
}

class Mario:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x, self.size_y = 40, 40
        self.frame = 0
        self.dir = 1
        self.velocity = 0
        self.jump_bool = False
        self.jump_power = 0
        self.speed = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.camera_x, self.camera_y = 0, 0
        if Mario.image == None:
            Mario.image = load_image('resource/mario.png.gif')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            try:
                history.append((self.cur_state.__name__, event_name[event]))
                self.cur_state.exit(self, event)
                self.cur_state = next_state_table[self.cur_state][event]
            except:
                print('cur state : ', self.cur_state.__name__, 'event : ', event_name[event])
                exit(-1)
            self.cur_state.enter(self, event)

        if self.jump_bool:
            if self.jump_power > -10:
                self.jump_power -= 3
            self.y += self.jump_power

        if self.y < 50: # 점프 테스트 용 맵과의 충돌처리로 변경
            self.y = 50
            self.jump_bool = False

    def draw(self):
        if self.jump_bool:
            if self.velocity == 1:
                self.image.clip_draw(144, 114, 18, 25, self.x - self.camera_x, self.y - self.camera_y, 40, 40)
            else:
                self.image.clip_draw(120, 114, 20, 24, self.x - self.camera_x, self.y - self.camera_y, 40, 40)
        else:
            self.cur_state.draw(self)
        # debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))
        debug_print(
            'velocity : ' + str(self.velocity) + ' dir : ' + str(self.dir) + 'state : ' + self.cur_state.__name__)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if (DEBUG_KEY == key_event):
                print(history[-4:])
            else:
                self.add_event(key_event)

    def jump_start(self):
        if not self.jump_bool:
            self.jump_bool = True
            self.jump_power = 20

    def fire_ball(self):
        pass



# def left_run(character):
#     if character.x_power > -0.5:
#         character.x_power -= 0.1
#     if(character.speed > -10.0):
#         character.speed += character.x_power
#
#     if character.jump_bool == False:
#         character.animation = 'left_run'
#
# def right_run(character):
#     if character.x_power < 0.5:
#         character.x_power += 0.1
#     if (character.speed < 10.0):
#         character.speed += character.x_power
#
#     if character.jump_bool == False:
#         character.animation = 'right_run'
#
# def standing(character):
#     if character.x_power > 0:
#         if character.jump_bool == False:
#             character.animation = 'right_standing'
#         character.x_power = 0
#     elif character.x_power < 0:
#         if character.jump_bool == False:
#             character.animation = 'left_standing'
#         character.x_power = 0
#
#     character.speed = 0
#
# def jump(character):
#     if character.jump_power > -15:
#         character.jump_power -= 2
#
#     character.y += character.jump_power
#
#
# def move(character, map):
#     character.x += character.speed
#
#     if character.jump_bool:
#         jump(character)
#     if character.state == 'left':
#         left_run(character)
#     elif character.state == 'right':
#         right_run(character)
#     else:
#         standing(character)
#
#     ground_collide(character, map)
#
#
# def monster_move(character):
#     if character.x > character.x_right:
#         character.state = 'left'
#         character.animation = 'left_run'
#     elif character.x < character.x_left:
#         character.state = 'right'
#         character.animation = 'right_run'
#
#     if character.state == 'left':
#         character.speed = -5.0
#     elif character.state == 'right':
#         character.speed = 5.0
#     else:
#         standing(character)
#
#     character.x += character.speed
#
# def draw(character, camera):
#     image = load_image(character.ani[character.animation].image_name)
#     if character.ani[character.animation].next_x_y:
#         image.clip_draw(
#             character.ani[character.animation].start_x + character.ani[character.animation].frame_now * character.ani[character.animation].next,
#             character.ani[character.animation].start_y,
#             character.ani[character.animation].width, character.ani[character.animation].height,
#             character.x - camera.start_x, character.y - camera.start_y, character.size_x, character.size_y)
#
#         if character.die == 'die_ani' and character.ani[character.animation].frame_now == character.ani[
#             character.animation].frame - 1:
#             character.die = 'die'
#         else:
#             character.ani[character.animation].frame_now = (character.ani[character.animation].frame_now + 1) % \
#                                                            character.ani[
#                                                                character.animation].frame
#     else:
#         image.clip_draw(
#             character.ani[character.animation].start_x,
#             character.ani[character.animation].start_y - character.ani[character.animation].frame_now * character.ani[
#                 character.animation].next,
#             character.ani[character.animation].width, character.ani[character.animation].height,
#             character.x - camera.start_x, character.y - camera.start_y, character.size_x, character.size_y)
#
#         if character.die == 'die_ani' and character.ani[character.animation].frame_now == character.ani[
#             character.animation].frame - 1:
#             character.die = 'die'
#             character.ani[character.animation].frame_now = (character.ani[character.animation].frame_now + 1) % \
#                                                            character.ani[character.animation].frame
#         else:
#             character.ani[character.animation].frame_now = (character.ani[character.animation].frame_now + 1) % character.ani[
#                 character.animation].frame
#
# def change_animation(character, ani_name):
#     character.animation = ani_name
#     character.ani[character.animation].frame_now = 0
#
# def draw_character(map, mario, all_goomba, all_koopagreen, camera):
#     draw(mario, camera)
#     for i in range(map.monster_number['goomba']):
#         if all_goomba[i].die == 'alive':
#             monster_move(all_goomba[i])
#             draw(all_goomba[i], camera)
#     for i in range(map.monster_number['koopagreen']):
#         if all_koopagreen[i].die == 'alive':
#             monster_move(all_koopagreen[i])
#             draw(all_koopagreen[i], camera)
#


