from random import choice
counter = 0
while counter < 100:
    print(counter)
    counter += choice(range(10))   # add a random number from 0 to 9 to counter
    # it will stop after the sum of counter is greater than 100

# second example: when I dont know how many iterations I will need
pop = 100
while 1:   # always do what is inside the loop because it is going to be true(while 1:)
    pop = pop*1.1  # increase population by pop*1.1
    if pop > 1000:
        break   # when the pop is over 1000, the while loop will stop
print("Final pop=", pop)