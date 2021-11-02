import game_framework
from pico2d import *
import gameover_state

from map import *
from interaction import *
from character import *

name = "MainState"

bk_ground = None
map = None
mario = None
camera = None

def enter():
    global bk_ground, map, mario, camera
    bk_ground = load_image('bg.png')

    map = Map(1600, 600, [[0] * 30 for _ in range(80)], 80, 30, {'goomba': 1, 'koopagreen': 1})
    map.tile_width = map.width // map.tile_x
    map.tile_height = map.height // map.tile_y

    for i in range(0, 39):
        map.tile_board[i][1] = 1
        map.tile_board[i][0] = 2

    for i in range(39, 55):
        map.tile_board[i][i - 37] = 3
        for j in range(0, i - 37):
            map.tile_board[i][j] = 2

    map.all_goomba = [
        Character('goomba', goomba_animation, 600, 50, 0, 'right', 'right_run', 50, 40, 600, 700, 'alive')]
    map.all_koopagreen = [
        Character('koopagreen', koopagreen_animation, 500, 50, 0, 'right', 'right_run', 25, 50, 500, 600, 'alive')]

    mario = Character('mario', small_mario_animation, 50, 50, 0, 'standing', 'right_standing', 40, 40, 0, 0, 'small')
    camera = Camera(400, 300, 800, 600)

def exit():
    global bk_ground, map, mario, camera
    del(bk_ground)
    del(map)
    del(mario)
    del(camera)


def handle_events():
    global running
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                mario.state = 'right'
                change_animation(mario, 'right_run')
            elif event.key == SDLK_a:
                mario.state = 'left'
                change_animation(mario, 'left_run')
            if event.key == SDLK_SPACE:
                if not mario.jump_bool:
                    mario.jump_bool = True
                    mario.jump_power = 17
                    if mario.speed > 0:
                        change_animation(mario, 'right_jump')
                    elif mario.speed < 0:
                        change_animation(mario, 'left_jump')
                    else:
                        if mario.animation == 'right_standing':
                            change_animation(mario, 'right_jump')
                        else:
                            change_animation(mario, 'left_jump')
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                mario.state = 'standing'
                mario.speed = 0
                change_animation(mario, 'right_standing')
            elif event.key == SDLK_a:
                mario.state = 'standing'
                mario.speed = 0
                # mario.speed += 10
                change_animation(mario, 'left_standing')


def draw():
    clear_canvas()
    bk_ground.draw(400, 300, 800, 600)
    draw_map(map, camera)
    draw_character(map, mario, map.all_goomba, map.all_koopagreen, camera)
    delay(0.005)
    update_canvas()







def update():
    if mario.die != 'die_ani':
        mario_with_monster(mario, map.all_goomba, map)
        mario_with_monster(mario, map.all_koopagreen, map)
    update_camera(camera, map, mario)
    move(mario, map)

    if mario.die == 'die':
        game_framework.change_state(gameover_state)

def pause():
    pass


def resume():
    pass
