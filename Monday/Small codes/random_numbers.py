#! /usr/bin/env python

import random
from numpy import zeros

# THERE ARE TWO SETS OF RANDOM FUNCTIONS!!!
# THE STANDARD ONES AND THE ONES FROM NP!

# Random float inside [0.0, 1.0)
print random.random()


# random.seed(46)
# After seeding, this always produces 0.888268076452
print random.random()


# 20 uniformly distributed random integers from 1 to 10
for i in range(1, 20+1, 1):
   rnd_number = random.random()
   #rnd_number = 0.99
   print int(1 + 10*rnd_number),
pass
print

print "Another way: 20 unif. distrib rnd intg from 1 to 10:"
# the last argument to randrange is the step size btw different values
for i in range(1, 20+1, 1):
   print random.randrange(1, 10+1, 1),
pass
print

print "\n--- Throwing a dye ---"
for i in range(1,50):
   print random.randrange(1, 6+1),
pass
print "\n---         ---"

# check values by building a histogram
h = zeros(11) # ignore index 0
print "h=", h
for i in range(1, 10000+1, 1):
   # using an explicit formula
   # rnd_int = int(1+10*random.random())
   # using built-in function
   rnd_int = random.randrange(1, 10+1, 1)
   # print rnd_int
   h[rnd_int] = h[rnd_int] +1
pass
print "h=", h
print "h norm =", h/10000


# value a or value b with equal probability
a = 5
b = 7
n_a = 0
n_b = 0
eps = 0.001
for i in range(1, 200+1, 1):
   r = random.random()
   x = (r<0.5)*a + (r>=0.5)*b
   if (abs(x-a) <= eps):
      #print "choosing a"
      n_a = n_a + 1
   if (abs(x-b) <= eps):
      #print "choosing b"
      n_b = n_b + 1
pass
print "n_a =", n_a
print "n_b =", n_b


# Generate 10 values of the normal distribution with mean=0 and std dev=1
import numpy as np
x = np.random.randn(10)
print "x = ", x

# This is .....what exactly
x = np.random.randn(10, 6, 30)
print x


# Generate an array of random integers from 1 to 6,
# in a 3x2 array
# Langtangen4: 814
print np.random.random_integers(1,6, size=(3, 2))



#coin = np.random.randint(1, 2)
#print coin
