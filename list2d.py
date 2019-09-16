from random import choice
list = [[choice((0,1)) for x in range(8)] for y in range(8)]
#   choose bwt 0 or 1 , range for x ,      range for y

for x in range(8):    # so it can be printed as a grid of 8x8
    print(list[x])     # y can be alos used instead of x