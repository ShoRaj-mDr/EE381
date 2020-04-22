'''
    The Simulation of a Continuous Uniform R.V.
    Using the histogram avaliable in python.
'''

import math
import random
import matplotlib.pyplot as plt

n = 1000000

x = []  	# Empty List for uniform
y = []  	# Empty List for exponential
Lambda = 0.5    # Parameter in exponential distribution
                # different betwn parameter and statistics
                # This "Lambda" is a parameter

for i in range (n) :
    r = random.uniform(0,1) 	# Discrete uniform
    x.append(r)            	# List of uniformly distributed random numbers
    e = (-1/Lambda)*math.log(1-r, math.e)   # inverse CDF
    y.append(e)     		# List of random exponentially distributed random numbers
#-----------------------------------------------------------------------------

b = max(x)
a = min(x)
R = b - a   			# Range of data

intervals = int (math.ceil (math.sqrt(n)))

width = (R / intervals)     	# Class Width


plt.subplot(2,1,1)
plt.hist(x, intervals, density = width)     # normed has been depricated.
plt.show()

plt.subplot(2,1,2)
plt.hist(y, intervals, density = width)     # the graph of the expontial RV
plt.show()

