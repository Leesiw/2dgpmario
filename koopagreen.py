from pico2d import *

history = []

DEBUG_KEY = range(1)

event_name = []

class RunState:
    def enter(koopagreen, event):
        koopagreen.speed = 1

    def exit(koopagreen, event):
        pass

    def do(koopagreen):
        koopagreen.frame = (koopagreen.frame + 1) % 8
        if koopagreen.x > koopagreen.next_x:
            koopagreen.velocity = -1
        elif koopagreen.x < koopagreen.start_x:
            koopagreen.velocity = 1

        koopagreen.x += koopagreen.velocity * koopagreen.speed
        koopagreen.x = clamp(25, koopagreen.x, 1600 - 25)

    def draw(koopagreen):
        if koopagreen.velocity == 1:
            koopagreen.image.clip_draw(48, 1328 - 32 * koopagreen.frame, 16, 32,
                                       koopagreen.x - koopagreen.camera_x, koopagreen.y - koopagreen.camera_y, 40, 40)
        else:
            koopagreen.image.clip_draw(0, 1328 - 32 * koopagreen.frame, 16, 32,
                                       koopagreen.x - koopagreen.camera_x, koopagreen.y - koopagreen.camera_y, 40, 40)


next_state_table = {
    RunState: {}
}

class KoopaGreen:
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
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.camera_x, self.camera_y = 0, 0

        if KoopaGreen.image == None:
            KoopaGreen.image = load_image('resource/koopagreen.png')

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


class All_koopagreen:
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

