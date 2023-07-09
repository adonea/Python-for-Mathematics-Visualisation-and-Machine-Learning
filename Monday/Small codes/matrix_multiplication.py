#! /usr/bin/env python
# From:
# McKinney - Python Data Analysis, p105

import numpy as np

#X = np.array([[1., 2., 3.], [4., 5., 6.]])
#Y = np.array([[6., 23.], [-1, 7], [8, 9]])

X = np.array([[1., 2., 3.], [4., 5., 6.]])
Y = np.array([[6., 23.], [-1, 7], [8, 9]])



print "X=\n", X
print "Y=\n", Y


prod = np.dot(X,Y)
print "X * Y =\n", prod

X = np.array([[0.0415, 0.9585], [0.000001, 0.999999]])
print X*X