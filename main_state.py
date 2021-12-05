import game_framework
import game_world
from pico2d import *
import gameover_state
import clear_state
import server

from stage import *

name = "MainState"

# bk_ground = None
# map = None
# mario = None
# camera = None




def enter():
    server.stage = Stage(1)

    game_world.add_object(server.stage.bk_ground, 0)
    game_world.add_object(server.stage.camera, 0)
    game_world.add_object(server.stage, 1)
    game_world.add_object(server.stage.all_box, 1)
    game_world.add_object(server.stage.all_item, 1)
    game_world.add_object(server.stage.all_monster, 1)
    game_world.add_object(server.stage.all_fireball, 1)
    game_world.add_object(server.stage.mario, 1)
    game_world.add_object(server.stage.ui, 1)

    import pickle

    with open('stage1.txt', 'wb') as f:
        pickle.dump(server.stage, f)


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
            server.stage.mario.handle_event(event)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw(server.stage.camera.start_x, server.stage.camera.start_y)
    update_canvas()







def update():
    if server.stage.ui.life_num == 0:
        game_framework.change_state(gameover_state)

    if server.stage.goal_in_bool and server.stage.next_id == 2 and server.stage.goal_timer + 5.0 < time.time():
        game_framework.change_state(clear_state)

    for game_object in game_world.all_objects():
        game_object.update()

    for b in server.stage.all_box.list:
        if b.hit_bool:
            if not len(b.item_que) == 0:
                state = b.item_que.pop()
                item = Item(state, b.x, b.y + b.height, 1)
                server.stage.all_item.list.append(item)


def pause():
    pass


def resume():
    pass
