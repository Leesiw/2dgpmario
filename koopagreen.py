from pico2d import *
import game_framework

history = []

DEBUG_KEY = range(1)
ALIVE, DIE = 0, 3
event_name = []

class RunState:
    def enter(koopagreen, event):
        pass

    def exit(koopagreen, event):
        pass

    def do(koopagreen):
        koopagreen.frame = (koopagreen.frame + koopagreen.action_speed * game_framework.frame_time) % 16
        if koopagreen.x > koopagreen.next_x:
            koopagreen.velocity = -1
        elif koopagreen.x < koopagreen.start_x:
            koopagreen.velocity = 1

        koopagreen.x += koopagreen.velocity * koopagreen.speed * game_framework.frame_time
        koopagreen.x = clamp(25, koopagreen.x, 1600 - 25)

    def draw(koopagreen, camera_x, camera_y):
        if koopagreen.velocity == 1:
            koopagreen.image.clip_draw(48, 1328 - 32 * int(koopagreen.frame), 16, 32,
                                       koopagreen.x - camera_x, koopagreen.y - camera_y, 40, 40)
        else:
            koopagreen.image.clip_draw(0, 1328 - 32 * int(koopagreen.frame), 16, 32,
                                       koopagreen.x - camera_x, koopagreen.y - camera_y, 40, 40)


class DieState:
    def enter(koopagreen, event):
        pass

    def exit(koopagreen, event):
        pass

    def do(koopagreen):
        koopagreen.frame = (koopagreen.frame + koopagreen.action_speed / 4 * game_framework.frame_time)

    def draw(koopagreen, camera_x, camera_y):
        koopagreen.image.clip_draw(0, 693 + 32 * int(koopagreen.frame), 25, 26,
                                   koopagreen.x - camera_x, koopagreen.y - camera_y, 50, 50)

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
        # 10pixel = 25cm, 12km/hour
        self.speed = (12.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
        self.action_speed = 1.0 / 0.05
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.state = ALIVE

        if KoopaGreen.image == None:
            KoopaGreen.image = load_image('resource/koopagreen.png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.state == DIE:
            self.cur_state = DieState
            self.cur_state.enter(self, None)
        self.cur_state.do(self)
        # if len(self.event_que) > 0:
        #     event = self.event_que.pop()
        #     try:
        #         history.append((self.cur_state.__name__, event_name[event]))
        #         self.cur_state.exit(self, event)
        #         self.cur_state = next_state_table[self.cur_state][event]
        #     except:
        #         print('cur state : ', self.cur_state.__name__, 'event : ', event_name[event])
        #         exit(-1)
        #     self.cur_state.enter(self, event)

    def draw(self, camera_x, camera_y):
        self.cur_state.draw(self, camera_x, camera_y)
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
            if i.state == DIE and i.frame > 1:
                self.list.remove(i)
            else:
                i.update()


