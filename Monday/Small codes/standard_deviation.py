#! /usr/bin/env python
#
# Sample standard deviation.
# With ddof=1, it corresponds to the definition in
# Introd Stat 3e / Ross 2010, page 103.
# s= sqrt (sum((xi-xbar)^2)  / (n-1) )
# Using data set A at page 99.

import numpy as np

x=np.array([1,2,5,6,6])

print x   # Output: [1 2 5 6 6]

print np.std(x, ddof=1)   # Output: 2.34520787991

