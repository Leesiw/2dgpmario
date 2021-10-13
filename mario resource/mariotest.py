from pico2d import *
from character import *
from map import *


def change_state(character, state):
    character.state_move = state
    character.ani[mario.state_move].frame_now = 0


def move(character):
    global frame
    character.x += character.speed
    if character.state_move == 'left_jump':
        if frame == character.ani['left_jump'].frame - 1:
            if character.speed == 0:
                change_state(character, 'left_standing')
            else:
                change_state(character, 'left_run')
    elif character.state_move == 'right_jump':
        if frame == character.ani['right_jump'].frame - 1:
            if character.speed == 0:
                change_state(character, 'right_standing')
            else:
                change_state(character, 'right_run')

def handle_events():
    global running
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.speed += 5
                change_state(mario, 'right_run')
            elif event.key == SDLK_LEFT:
                mario.speed -= 5
                change_state(mario, 'left_run')
            if event.key == SDLK_SPACE:
                if mario.speed > 0:
                    change_state(mario, 'right_jump')
                elif mario.speed < 0:
                    change_state(mario, 'left_jump')
                else:
                    if mario.state_move == 'right_standing':
                        change_state(mario, 'right_jump')
                    else:
                        change_state(mario, 'left_jump')
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                mario.speed -= 5
                change_state(mario, 'right_standing')
            elif event.key == SDLK_LEFT:
                mario.speed += 5
                change_state(mario, 'left_standing')


open_canvas()

bk_ground = load_image('bg.png')
mario_image = load_image('mario.png.gif')



running = True
speed = 0
frame = 0

while running:
    bk_ground.draw(400, 300, 800, 600)
    draw_map(test_map, test_map.tile_name)
    mario_image.clip_draw(mario.ani[mario.state_move].start_x + mario.ani[mario.state_move].frame_now * mario.ani[mario.state_move].next,
                          mario.ani[mario.state_move].start_y,
                          mario.ani[mario.state_move].width, mario.ani[mario.state_move].height,
                          mario.x, mario.y, mario.size_x, mario.size_y)
    mario.ani[mario.state_move].frame_now = (mario.ani[mario.state_move].frame_now + 1) % mario.ani[mario.state_move].frame
    update_canvas()
    handle_events()
    move(mario)
    delay(0.05)

close_canvas()
