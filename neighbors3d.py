from random import choice
n = 100   # grid of 100x100
count = 0   # to keep track
nocc = 0    # to keep track of occupied cells

# initialization of the 3D array
list3d = [[[choice((0, 1)) for x in range(n)] for y in range(n)] for z in range(n)]

for x in range(1, n-1):   # from 1 to 98 on x
    for y in range(1, n-1):   # from 1 to 98 on y
        for z in range(1, n-1):   # from 1 to 98 on z
            if list3d[x][y][z] == 1:   # if cell is occuppied
                nocc += 1    # if cell is occpied, add 1 to nocc
                # indicating the neighbors cells
                neigh = list3d[x-1][y][z]+list3d[x+1][y][z]+\
                list3d[x][y-1][z]+list3d[x][y+1][z]+\
                list3d[x][y][z-1]+list3d[x][y][z+1]

                if neigh > 2:  #if the occupied cell has more than 2 occuppied cells
                    count += 1
print("Fraction with more than 2 neighbors in 3-D is:", count/nocc)