N = 70   # random especific value
steps = 0

while N != 1:   # continue in the while as the steps is not 1
    print(N)
    steps += 1   #increment the counter, keep in track of the steps

    if N%2 == 0:   # condition of even numbers
        N = N//2  # if N is even, then N= N/2

    else:    #Condition of odd numbers
        N = 3*N + 1   # if N is odd, then N = 3*N + 1
print("N=1 and it took", steps, "steps")