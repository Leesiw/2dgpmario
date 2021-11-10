import game_framework
import game_world
from pico2d import *
import gameover_state

from map import *
from interaction import *
from mario import *
from bkground import *

name = "MainState"

# bk_ground = None
# map = None
# mario = None
# camera = None

def enter():
    global mario
    mario = Mario(600, 50)
    bk_ground = Bkground()
    game_world.add_object(bk_ground, 0)
    game_world.add_object(mario, 1)

def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mario.handle_event(event)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    # bk_ground.draw(400, 300, 800, 600)
    # draw_map(map, camera)
    # draw_character(map, mario, map.all_goomba, map.all_koopagreen, camera)
    # delay(0.005)
    update_canvas()







def update():
    delay(0.01)
    for game_object in game_world.all_objects():
        game_object.update()
    # if mario.die != 'die_ani':
    #     mario_with_monster(mario, map.all_goomba, map)
    #     mario_with_monster(mario, map.all_koopagreen, map)
    # update_camera(camera, map, mario)
    # move(mario, map)
    #
    # if mario.die == 'die':
    #     game_framework.change_state(gameover_state)

def pause():
    pass


def resume():
    pass
