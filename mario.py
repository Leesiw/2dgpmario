from pico2d import *
import game_framework

history = []

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, DEBUG_KEY = range(6)

event_name = ['RIGHT_DOWN', 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP', 'SPACE']

SMALL, BIG, FIRE, DIE = range(4)

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
        mario.frame = (mario.frame + mario.action_speed * game_framework.frame_time) % 9

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(2 + int(mario.frame) * 20, 192, 20, 23, mario.x - mario.camera_x, mario.y - mario.camera_y,
                                  mario.size_x, mario.size_y)
        else:
            mario.image.clip_draw(2 + int(mario.frame) * 20, 215, 18, 24, mario.x - mario.camera_x, mario.y - mario.camera_y,
                                  mario.size_x, mario.size_y)

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
        if event == SPACE:
            mario.jump_start()

    def do(mario):
        mario.frame = (mario.frame + mario.action_speed * game_framework.frame_time) % 12

        mario.x += mario.velocity * mario.speed * game_framework.frame_time
        # mario.x = clamp(25, mario.x, 1600 - 25)

    def draw(mario):
        if mario.velocity == 1:
            mario.image.clip_draw(2 + int(mario.frame) * 20, 143, 20, 24, mario.x - mario.camera_x, mario.y - mario.camera_y,
                                  mario.size_x, mario.size_y)
        else:
            mario.image.clip_draw(3 + int(mario.frame) * 20, 168, 20, 24, mario.x - mario.camera_x, mario.y - mario.camera_y,
                                  mario.size_x, mario.size_y)

class DieState:
    def enter(mario, event):
        mario.state = DIE

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + mario.action_speed / 2 * game_framework.frame_time)

    def draw(mario):
        mario.image.clip_draw(50 + int(mario.frame) * 25, 27, 25, 24, mario.x - mario.camera_x,mario.y - mario.camera_y
                              , mario.size_x, mario.size_y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    DieState: {RIGHT_UP: DieState, LEFT_UP: DieState, LEFT_DOWN: DieState, RIGHT_DOWN: DieState, SPACE: DieState}
}

class Mario:
    image = None
    name = 'mario'

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x, self.size_y = 40, 40
        self.frame = 0
        self.dir = 1
        self.velocity = 0
        self.jump_bool = False
        self.jump_power = 0
        self.jump_power_first = 80.0
        # 10pixel = 25cm, 20km/hour
        self.speed = (20.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
        self.action_speed = 1.0 / 0.05
        self.event_que = []
        self.life_number = 3
        self.g = (35.3094 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.camera_x, self.camera_y = 0, 0
        self.state = SMALL
        self.unbeatable = False
        self.unbeatable_timer = 0.0
        self.on_box = False
        self.time = 0.0
        if Mario.image == None:
            Mario.image = load_image('resource/mario.png.gif')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.state == DIE and not self.cur_state == DieState:
            self.state = DIE
            self.cur_state = DieState
            self.frame = 0
            self.cur_state.enter(self, None)
            print(self.frame)
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
            current_time = game_framework.time.time() - self.time
            self.jump_power -= self.g * current_time
            self.y += self.jump_power * game_framework.frame_time

    def draw(self):
        if self.jump_bool:
            if self.dir == 1:
                self.image.clip_draw(144, 114, 18, 25, self.x - self.camera_x, self.y - self.camera_y, self.size_x, self.size_y)
            else:
                self.image.clip_draw(120, 114, 20, 24, self.x - self.camera_x, self.y - self.camera_y, self.size_x, self.size_y)
        else:
            self.cur_state.draw(self)
        # debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))
        # debug_print(
            # 'velocity : ' + str(self.velocity) + ' dir : ' + str(self.dir) + ' state : ' + self.cur_state.__name__ + ' frame : ' + str(self.frame))

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
            self.jump_power = (self.jump_power_first * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
            self.time = game_framework.time.time()

    def fire_ball(self):
        pass

