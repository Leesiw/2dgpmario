def mario_with_monster(mario, monster):
    if 0 < mario.x - monster.x < monster.size_x or 0 < monster.x - mario.x < mario.size_x:
        if 0 < monster.y + monster.size_y - mario.y < mario.size_y / 5:
            print("monster die")
        elif mario.y < monster.y + monster.size_y:
            print("mario die")



