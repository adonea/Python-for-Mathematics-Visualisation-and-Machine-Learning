#! /usr/bin/env python

import numpy as np


# Using example 2, page 272, Wylie
X = np.array(
[[ 4.0, -5.0 ],
 [ 1.0, -2.0 ]]
)

# Solution (python normalizes):
# lambda1 = -1 ---> x1=[1, 1] ---> [1/sqrt(2),  1/sqrt(2)]
# lambda2 = 3  ---> x2=[5, 1] ---> [5/sqrt(26), 1/sqrt(26)]




# Eigenvalues and eigenvectors
print "========================"
evals, evecs = np.linalg.eig(X)

#print evals
#print evecs
#print evals[0], evecs[0]


# From http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html
#print "http://///////////////"
#evals, evecs = np.linalg.eig(np.diag((1, 2, 3)))

#print evals
#print len(evals)

for i in range(0, len(evals), 1):
   print "eval=", evals[i], "evec =", evecs[:,i]

