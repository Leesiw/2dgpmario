def mario_with_monster(mario, monster, map):
    for i in range(map.monster_number[monster[0].name]):
        if monster[i].die == 'alive':
            if 0 < mario.x - monster[i].x < monster[i].size_x or 0 < monster[i].x - mario.x < mario.size_x:
            # if 0 < monster[i].x + monster[i].size_x / 2 - mario.x < mario.size_x:
                if 0 < monster[i].y + monster[i].size_y - mario.y < mario.size_y / 5:
                    monster[i].die = 'die_ani'
                    monster[i].ani['die'].frame_now = 0
                    monster[i].animation = 'die'
                    mario.jump_bool = True
                    mario.jump_power = 10
                    # print('monster die')
                elif mario.y < monster[i].y + monster[i].size_y:
                    mario.die = 'die_ani'
                    mario.frame_now = 0
                    mario.animation = 'die'
                    # print('mario die')


