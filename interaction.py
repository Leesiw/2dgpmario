import time
DIE = 3

def mario_with_monster(m, monster):
    if m.unbeatable:
        # print('unbeatable')
        return
    if 0 < m.x - monster.x < monster.size_x or 0 < monster.x - m.x < m.size_x:
        if 0 < monster.y + monster.size_y - m.y < m.size_y / 2:
            monster.state = DIE
            monster.frame = 0
            m.jump_bool = True
            m.jump_power = (30.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
            m.time = time.time()
        elif m.y < monster.y + monster.size_y:
            if m.state == 0:
                m.state = DIE
            elif m.state == 1:
                m.state = 0
                m.jump_power_first = 50.0
                m.size_y = 40
                m.unbeatable = True
                m.unbeatable_timer = time.time()
            elif m.state == 2:
                m.state = 1
                m.unbeatable = True
                m.unbeatable_timer = time.time()

def mario_with_goomba(m, goomba):
    if goomba.velocity == 1:
        if goomba.x < m.x < goomba.x + 200: # 200pixel = 5m
            goomba.add_event(0)     # SEE_MARIO
        else:
            goomba.add_event(1)  # MISS_MARIO
    else:
        if goomba.x - 200 < m.x < goomba.x:
            goomba.add_event(0)     # SEE_MARIO
        else:
            goomba.add_event(1)  # MISS_MARIO


def mario_with_item(m, item):
    if 0 < m.x - item.x < item.size_x or 0 < item.x - item.x < item.size_x:
        if 0 < item.y + item.size_y - m.y < m.size_y / 2:
            if item.type == 0:
                if m.state == 0:
                    m.state = 1
                    m.jump_power_first = 70.0
                    m.size_y = 60
            elif item.type == 1:
                m.life_number += 1
            elif item.type == 2:
                m.state = 2
                m.jump_power_first = 70.0
                m.size_y = 60
                m.fire_bool = True
            return True

def fireball_with_monster(f, monster):
    if f.x - f.size_x < monster.x + monster.size_x and f.x + f.size_x > monster.x - monster.size_x:
        if f.y - f.size_y < monster.y + monster.size_y and f.y + f.size_y > monster.y - monster.size_y:
            monster.state = DIE
            monster.frame = 0
            return True
    return False

