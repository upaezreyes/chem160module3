from random import choice
side = 4   # [0,1,2,3]
x = 0    # to keep record of x

for i in range(40):     #30 times
    x += choice((-1,1))   # Randomly moving, eitheir forward or backward

    if x < 0:    # if the location is zero, than it start from 3 (the right side)
        x = side - 1
    if x ==side:   # if the position is 3 (the ringht end) than it will move starting from 0
        x = 0    # start from 0 ( the left side)
    print(x)
