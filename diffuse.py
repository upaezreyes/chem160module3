from random import choice
npart=300  # Total number of particles
side=55   # This is the grid , should be an odd number
time = 0   # To keep track of time
steps = [(1,0),(-1,0),(0,1),(0,-1)]   # 4 different possible ways the particle can move
grid=[[0 for x in range(side)] for y in range(side)]

for ipart in range(npart):
    # Start particle at the center of the box
    x,y = side//2,side//2
    counter = 0    # to calculate how long it takes for the particle to move out of the box

    # perform the random walk until particle aggregates
    while 1:
        counter += 1     # to increment the counter
        grid[x][y]=0   #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy

        if x<0 or y<0 or x==side or y==side:
            time += counter
            break
        grid[x][y]=1   #Put particle in new location

averagetime = time/npart
print("<t>=%5.2f <t>/r2=%5.2f"%(averagetime,averagetime/(side**2)))