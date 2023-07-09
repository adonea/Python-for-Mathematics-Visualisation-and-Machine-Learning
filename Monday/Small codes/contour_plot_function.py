#! /usr/bin/env python

# Is there a better way
# Example from Matplotlib for Python Developers, by Sandro Tosi, Packt 2009


import matplotlib.pyplot as plt;
import numpy as np

x = np.arange(-2, 2, 0.001)
y = np.arange(-2, 2, 0.001)
X, Y = np.meshgrid(x,y)


function_X_Y = X*X*X + Y*Y*Y - 2 * X -Y


cs = plt.contour(function_X_Y)
plt.clabel(cs)
plt.show()
