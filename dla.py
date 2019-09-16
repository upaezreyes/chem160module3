from random import choice
from drawgridlib import drawgrid
npart=700   # The total of particles
side=75  #Should be an odd number
steps = [(1,0),(-1,0),(0,1),(0,-1)]   # 4 different possible ways the particle can move
grid=[[0 for x in range(side)] for y in range(side)]
grid[side//2][side//2]=1

for ipart in range(npart):
    # Start particle at origin
    x,y = 0,0

    # Perform the random walk until particle agrregates
    while 1:   # the particle will continue working until we tell it to break
        grid[x][y] = 0  # Remove particle from current position

        #Randomly move particle
        sx,sy = choice(steps)   # chage of x and y (where particle will move) randomly picks from choice(steps)
        x += sx    # keep track of the particle moving to the x direction
        y += sy     # keep track of the particle moving to the y direction

        # Enforce periodic boundaries
        if x < 0:  # if moves x<0, start from the other side
            x = side - 1
        if y < 0:
            y = side - 1
        if x == side:
            x = 0
        if y == side:
            y = 0

        grid[x][y]=1  # Put particle in new location

        # Stop if you are next to a particle
        if (grid[(x+1)%side][y]+grid[x][(y+1)%side]+
            grid[(x+side-1)%side][y]+grid[x][(y+side-1)%side])>0:
            break
drawgrid(grid,side)