#! /usr/bin/env python

import numpy as np
from numpy import zeros
from numpy import array

x = np.array([1, 2, 3])
print "x = ", x
print "len(x) = ", len(x)

y = 2 * x
print "y = ", y

z = x + y
print z

a = zeros(3)
print "a = ", a

# Loop over elements in x
for xi in x:
   print "element of x = ", xi


# Another way of looping
for i in range(len(x)):
   print "element %d = %f" % (i, x[i])



# Initialising an array
w = array([[4, 3, 6, 5],
           [1, 4, 8, 8],
           [5, 7, 6, 3]])
print "w = \n", w
print w.shape
print "w[0][0] = ", w[0][0]
print "w[0] = ", w[0]



# Loop over first index of w ?
# w = wi,j
# for x in w[x] print x


# Arrays can be divided!!!!
a1 = array([2, 9, 16])
a2 = array([2, 3, 4])
print a1/a2
# Output:
# [1 3 4]