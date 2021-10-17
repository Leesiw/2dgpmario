from pico2d import *
from character import *
from map import *
from interaction import *

def draw_character():
    draw(mario, camera)
    for i in range(test_map.monster_number['goomba']):
        if all_goomba[i].die == 'alive':
            monster_move(all_goomba[i])
            draw(all_goomba[i], camera)
    for i in range(test_map.monster_number['koopagreen']):
        if all_koopagreen[i].die == 'alive':
            monster_move(all_koopagreen[i])
            draw(all_koopagreen[i], camera)

def change_animation(character, ani_name):
    character.animation = ani_name
    character.ani[mario.animation].frame_now = 0

def restart():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == 'r':
                mario.die = 'small'
                mario.animation = 'right_run'

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.state = 'right'
                change_animation(mario, 'right_run')
            elif event.key == SDLK_LEFT:
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
            if event.key == SDLK_RIGHT:
                mario.state = 'standing'
                mario.speed = 0
                change_animation(mario, 'right_standing')
            elif event.key == SDLK_LEFT:
                mario.state = 'standing'
                mario.speed = 0
                # mario.speed += 10
                change_animation(mario, 'left_standing')


open_canvas()

bk_ground = load_image('bg.png')
mario_image = load_image('mario.png.gif')
game_over = load_image('gameover.png')
mario.small_big = 'small'

running = True
speed = 0
frame = 0
die = False

while running:
    if mario.die != 'die':
        bk_ground.draw(400, 300, 800, 600)
        update_camera(camera, test_map, mario)
        draw_map(test_map, camera)
        if mario.die != 'die_ani':
            mario_with_monster(mario, all_goomba, test_map)
            mario_with_monster(mario, all_koopagreen, test_map)

        draw_character()

        update_canvas()
        handle_events()
        move(mario)
        delay(0.005)
    else:
        game_over.draw(400, 300, 800, 600)
        restart()
        update_canvas()

close_canvas()
