import time
DIE = 3

def mario_with_monster(m, monster):
    if 0 < m.x - monster.x < monster.size_x or 0 < monster.x - m.x < m.size_x:
        if 0 < monster.y + monster.size_y - m.y < m.size_y / 2:
            monster.state = DIE
            monster.frame = 0
            m.jump_bool = True
            m.jump_power = (20.0 * 1000.0 / 60.0) / 60.0 * 10.0 / 0.25
            m.time = time.time()
        elif m.y < monster.y + monster.size_y:
            m.state = DIE

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
