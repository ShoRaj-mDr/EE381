'''
Discription: Simulate a Bernoulli
Random Variable and use it to make a Markov process
'''
import random

p = float(input("Enter the probability of success. "))
T = int(input('Enter number of trails. '))

for j in range(T):
    r = random.uniform(0,1)
    if r < p:
        print('1', end=' ')     # Success rate
    else:
        print('0', end=' ')     # Failure rate

print("\n")
