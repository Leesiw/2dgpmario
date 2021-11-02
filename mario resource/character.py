from animation import *
from camera import *
from map import *

class Character:
    def __init__(self, name, ani, x, y, speed, state, animation, size_x, size_y, x_left, x_right, die):
        self.name = name
        self.ani = ani
        self.x = x
        self.y = y
        self.speed = speed
        self.state = state
        self.animation = animation
        self.size_x = size_x
        self.size_y = size_y
        self.jump_bool = False
        self.jump_power = 0
        self.x_power = 0
        self.looking_at = True
        self.x_left = x_left
        self.x_right = x_right
        self.die = die

def left_run(character):
    if character.x_power > -0.5:
        character.x_power -= 0.1
    character.speed += character.x_power

    if character.jump_bool == False:
        character.animation = 'left_run'

def right_run(character):
    if character.x_power < 0.5:
        character.x_power += 0.1
    character.speed += character.x_power

    if character.jump_bool == False:
        character.animation = 'right_run'

def standing(character):
    if character.x_power > 0:
        if character.jump_bool == False:
            character.animation = 'right_standing'
        character.x_power -= 0
    elif character.x_power < 0:
        if character.jump_bool == False:
            character.animation = 'left_standing'
        character.x_power += 0

    character.speed = 0

def jump(character):
    if character.jump_power > -15:
        character.jump_power -= 2

    character.y += character.jump_power


def move(character, map):
    character.x += character.speed

    if character.jump_bool:
        jump(character)
    if character.state == 'left':
        left_run(character)
    elif character.state == 'right':
        right_run(character)
    else:
        standing(character)

    ground_collide(character, map)


def monster_move(character):
    if character.x > character.x_right:
        character.state = 'left'
        character.animation = 'left_run'
    elif character.x < character.x_left:
        character.state = 'right'
        character.animation = 'right_run'

    if character.state == 'left':
        character.speed = -5.0
    elif character.state == 'right':
        character.speed = 5.0
    else:
        standing(character)

    character.x += character.speed

def draw(character, camera):
    image = load_image(character.ani[character.animation].image_name)
    if character.ani[character.animation].next_x_y:
        image.clip_draw(
            character.ani[character.animation].start_x + character.ani[character.animation].frame_now * character.ani[character.animation].next,
            character.ani[character.animation].start_y,
            character.ani[character.animation].width, character.ani[character.animation].height,
            character.x - camera.start_x, character.y - camera.start_y, character.size_x, character.size_y)

        if character.die == 'die_ani' and character.ani[character.animation].frame_now == character.ani[
            character.animation].frame - 1:
            character.die = 'die'
        else:
            character.ani[character.animation].frame_now = (character.ani[character.animation].frame_now + 1) % \
                                                           character.ani[
                                                               character.animation].frame
    else:
        image.clip_draw(
            character.ani[character.animation].start_x,
            character.ani[character.animation].start_y - character.ani[character.animation].frame_now * character.ani[
                character.animation].next,
            character.ani[character.animation].width, character.ani[character.animation].height,
            character.x - camera.start_x, character.y - camera.start_y, character.size_x, character.size_y)

        if character.die == 'die_ani' and character.ani[character.animation].frame_now == character.ani[
            character.animation].frame - 1:
            character.die = 'die'
            character.ani[character.animation].frame_now = (character.ani[character.animation].frame_now + 1) % \
                                                           character.ani[character.animation].frame
        else:
            character.ani[character.animation].frame_now = (character.ani[character.animation].frame_now + 1) % character.ani[
                character.animation].frame

def change_animation(character, ani_name):
    character.animation = ani_name
    character.ani[character.animation].frame_now = 0

def draw_character(map, mario, all_goomba, all_koopagreen, camera):
    draw(mario, camera)
    for i in range(map.monster_number['goomba']):
        if all_goomba[i].die == 'alive':
            monster_move(all_goomba[i])
            draw(all_goomba[i], camera)
    for i in range(map.monster_number['koopagreen']):
        if all_koopagreen[i].die == 'alive':
            monster_move(all_koopagreen[i])
            draw(all_koopagreen[i], camera)



