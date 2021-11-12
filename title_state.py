import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
font = None

def enter():
    global image, font
    image = load_image('resource/title.png')
    font = load_font('resource/SuperMario256.ttf', 30)

def exit():
    global image, font
    del(image)
    del(font)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    font.draw(300, 100, 'PRESS SPACE', (0, 0, 0))
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass

