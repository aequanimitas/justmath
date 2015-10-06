import random

def die_roll_generator(rolls = 3, faces = 6):
    drg = {x: None for x in range(1,rolls + 1)}
    for x in drg:
        drg[x] = (random.randrange(1,faces), random.randrange(1, faces))
    return drg
