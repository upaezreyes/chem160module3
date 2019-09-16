from random import choice
n = 200   # grid of 100x100
count = 0   # to count the total number of neighbors a particular cell has
nocc = 0    # to keep track of cells occuppied

list = [[choice((0,1)) for x in range(n)] for y in range(n)]

for x in range(1, n-1):    # Loop from 1 to 98, not using the edges
    for y in range(1, n-1):   #Loop from 1 to 98, not using the edges
        if list[x][y] == 1:   # this mean the cell is occupied
            nocc += 1   # if the cell is occupied, it will increment nocc

           #adding the neighbores
            neigh = list[x-1][y] + list[x+1][y] + list[x][y-1] + list[x][y+1]
                   #(x-1)(y)       (x+1)(y)       (x)(y-1)       (x)(y+1)
            if neigh > 2:  # if the cell has more than 2 occupied neighbors
               count += 1 #keep count of the cell with more than 2 neighbors
print("Fraction with more than 2 neighbors:", count/nocc)