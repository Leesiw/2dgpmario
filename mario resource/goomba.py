from pico2d import *

history = []
SEE_MARIO, MISS_MARIO, DEBUG_KEY = range(3)

event_name = ['SEE_MARIO', 'MISS_MARIO']

class RunState:
    def enter(goomba, event):
        goomba.speed = 1

    def exit(goomba, event):
        pass

    def do(goomba):
        goomba.frame = (goomba.frame + 1) % 8
        if goomba.x > goomba.next_x:
            goomba.velocity = -1
        elif goomba.x < goomba.start_x:
            goomba.velocity = 1

        goomba.x += goomba.velocity * goomba.speed
        goomba.x = clamp(25, goomba.x, 1600 - 25)

    def draw(goomba):
        if goomba.velocity == 1:
            goomba.image.clip_draw(50, 867 - 31 * goomba.frame, 30, 30, goomba.x, goomba.y, 40, 40)
        else:
            goomba.image.clip_draw(0, 867 - 31 * goomba.frame, 30, 30, goomba.x, goomba.y, 40, 40)


class DashState:
    def enter(goomba, event):
        goomba.speed = 5
        goomba.dir = goomba.velocity

    def exit(goomba, event):
        pass
    def do(goomba):
        goomba.frame = (goomba.frame + 1) % 8

        goomba.x += goomba.velocity * goomba.speed
        goomba.x = clamp(25, goomba.x, 1600 - 25)

    def draw(goomba):
        if goomba.velocity == 1:
            goomba.image.clip_draw(50, 867 - 31 * goomba.frame, 30, 30, goomba.x, goomba.y, 40, 40)
        else:
            goomba.image.clip_draw(0, 867 - 31 * goomba.frame, 30, 30, goomba.x, goomba.y, 40, 40)


next_state_table = {
    DashState: {SEE_MARIO: DashState, MISS_MARIO: RunState},
    RunState: {SEE_MARIO: DashState, MISS_MARIO: RunState}
}

class Goomba:
    image = None

    def __init__(self, x, y, next_x):
        self.x, self.y = x, y
        self.start_x = x
        self.next_x = next_x
        self.frame = 0
        self.velocity = 1
        self.speed = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        if Goomba.image == None:
            Goomba.image = load_image('goomba.png')

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

    def draw(self):
        self.cur_state.draw(self)
        # debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))
        # debug_print(
        #     'velocity : ' + str(self.velocity) + ' dir : ' + str(self.dir) + 'state : ' + self.cur_state.__name__)


class All_goomba:
    list = None

    def __init__(self, num):
        self.num = num
        self.list = []

    def update(self):
        for i in self.list:
            i.update()

    def draw(self):
        for i in self.list:
            i.draw()


