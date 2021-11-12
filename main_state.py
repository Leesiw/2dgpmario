import game_framework
import game_world
from pico2d import *
import gameover_state

from stage import *

name = "MainState"

# bk_ground = None
# map = None
# mario = None
# camera = None

def enter():
    global stage
    stage = Stage(1)

    game_world.add_object(stage.bk_ground, 0)
    game_world.add_object(stage, 1)
    game_world.add_object(stage.all_monster, 1)
    game_world.add_object(stage.mario, 1)

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
            stage.mario.handle_event(event)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







def update():
    if stage.mario.state == DIE and stage.mario.frame > 5:
        game_framework.change_state(gameover_state)

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
