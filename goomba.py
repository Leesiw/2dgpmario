from pico2d import *
import game_framework

history = []
SEE_MARIO, MISS_MARIO, DEBUG_KEY = range(3)

ALIVE, DIE = 0, 3

event_name = ['SEE_MARIO', 'MISS_MARIO']

G = (35.3094 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25

class RunState:
    def enter(goomba, event):
        # 10pixel = 25cm, 10km/hour
        goomba.speed = (10.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25

    def exit(goomba, event):
        pass

    def do(goomba):
        goomba.frame = (goomba.frame + goomba.action_speed * game_framework.frame_time) % 8
        if goomba.x > goomba.next_x:
            goomba.velocity = -1
        elif goomba.x < goomba.start_x:
            goomba.velocity = 1

        goomba.x += goomba.velocity * goomba.speed * game_framework.frame_time
        goomba.x = clamp(25, goomba.x, 1600 - 25)

    def draw(goomba, camera_x, camera_y):
        if goomba.velocity == 1:
            goomba.image.clip_draw(50, 867 - 31 * int(goomba.frame), 30, 30, goomba.x - camera_x, goomba.y - camera_y, 40, 40)
        else:
            goomba.image.clip_draw(0, 867 - 31 * int(goomba.frame), 30, 30, goomba.x - camera_x, goomba.y - camera_y, 40, 40)


class DashState:
    def enter(goomba, event):
        # 10pixel = 25cm, 17km/hour
        goomba.speed = (17.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
        goomba.dir = goomba.velocity

    def exit(goomba, event):
        pass
    def do(goomba):
        goomba.frame = (goomba.frame + goomba.action_speed * game_framework.frame_time) % 8

        goomba.x += goomba.velocity * goomba.speed * game_framework.frame_time
        goomba.x = clamp(25, goomba.x, 1600 - 25)

    def draw(goomba, camera_x, camera_y):
        if goomba.velocity == 1:
            goomba.image.clip_draw(50, 867 - 31 * int(goomba.frame), 30, 30, goomba.x - camera_x, goomba.y - camera_y, 40, 40)
        else:
            goomba.image.clip_draw(0, 867 - 31 * int(goomba.frame), 30, 30, goomba.x - camera_x, goomba.y - camera_y, 40, 40)

class DieState:
    def enter(goomba, event):
        pass

    def exit(goomba, event):
        pass

    def do(goomba):
        goomba.frame = (goomba.frame + goomba.action_speed / 4 * game_framework.frame_time)

    def draw(goomba, camera_x, camera_y):
        goomba.image.clip_draw(5, 614 - 31 * int(goomba.frame), 30, 30, goomba.x - camera_x, goomba.y - camera_y, 40, 40)

next_state_table = {
    DashState: {SEE_MARIO: DashState, MISS_MARIO: RunState},
    RunState: {SEE_MARIO: DashState, MISS_MARIO: RunState},
    DieState: {SEE_MARIO: DieState, MISS_MARIO: DieState}
}

class Goomba:
    image = None

    def __init__(self, x, y, next_x):
        self.x, self.y = x, y
        self.size_x, self.size_y = 40, 40
        self.jump_bool = False
        self.start_x = x
        self.next_x = next_x
        self.frame = 0
        self.velocity = 1
        self.speed = 0
        self.state = ALIVE
        self.action_speed = 1.0 / 0.05
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.on_box = False

        if Goomba.image == None:
            Goomba.image = load_image('resource/goomba.png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.state == DIE:
            self.cur_state = DieState
            self.cur_state.enter(self, None)
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
            self.jump_power -= G * current_time
            self.y += self.jump_power * game_framework.frame_time
    def draw(self, camera_x, camera_y):
        self.cur_state.draw(self, camera_x, camera_y)


class All_goomba:
    list = None
    def __init__(self, num):
        self.num = num
        self.list = []

    def update(self):
        for i in self.list:
            if i.state == DIE and i.frame > 2:
                self.list.remove(i)
            else:
                i.update()




