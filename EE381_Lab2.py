""" 
Discription: This is the solution via simulation of a probability
problem. What is the probability of a head on an odd flip? 
"""

win = 0     # Accumulator
T = 1000   # Outer Loop

for i in range(T):

    #----------------------------------------------
    Coin = 0    # Initial value of variable is 'tails' or zero.
    a = 0       # Accumulator counting coin flips.
    import math

    #----------------------------------------------
    # Constants
    N = 1000    # The norm
    A = 4857    # The adder
    M = 8601    # The multiplier. 
    #----------------------------------------------

    #Get seed from clock
    import time
    S = time.time_ns() - time.process_time_ns()
    #----------------------------------------------

    # for i in range(25):
    while (Coin == 0):
        a = a + 1
        S = (M * S + A) % N     # RNG formula
        v = S / N               # Numbers in [0,1)
        time.sleep(0.0025)
        Coin = math.floor(2*v)
    if (a % 2 == 1):
        win = win + 1

print(win/T)


