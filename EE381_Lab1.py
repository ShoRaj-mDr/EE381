
# EE 381 Spring 2020 Project 1
# Python- lab Assingment 1
# Name: Shoraj Manandhar
# I.D. #: 025307085
# Start Date: 1-27-2020
# End Date: 1-29-2020
# Discription: This is the code for a pseudorandom number generator, RNG.
# It will output a uniform distribution of number in the set [0,1).

def main():

        def RNG():

                r = [] #List of random numbers.
                #------------------------------------------------------------------------
                # Constants 
                N = 10000       # the norm.
                A = 4857        # the adder.
                M = 8601        # the multiplier.
                #------------------------------------------------------------------------
                # Get seed from clock
                import time
                S = time.time() - time.process_time()
                #------------------------------------------------------------------------

                for i in range(25):
                        S = (M * S + A) % N      # RNG
                        v = S / N                 # numbers in [0,1)
                        r.append(v)
                return r

        def die(d):
                import math
                print('Die Roll')
                for k in range(25):
                        die = math.floor(6 * d[k] + 1)
                        die = str(die)
                        print(die, end= ' ')
        
        def coin(c):
                import math
                print('\n')
                print('Coin Toss')
                for k in range(25):
                        coin = math.floor(2*c[k])
                        if coin == 0:
                                print('T', end=' ')
                        else:
                                print('H', end=' ')
                print('\n')

        r = RNG()
        die(r)
        coin(r)

main()
