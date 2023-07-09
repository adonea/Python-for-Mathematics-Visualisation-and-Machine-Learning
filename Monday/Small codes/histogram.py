#! /usr/bin/env python
#
# Example or exercise from introductory Statistics, 3e / Ross 2010

import numpy as np
import matplotlib.pyplot as plt

x=np.array([752, 532, 132, 119, 117, 736, 462, 540, 829, 1164, 635, 450])

print min(x), max(x)

xmin=100;
xmax=1200;
bin_size=100

bins=np.arange(xmin, xmax+bin_size, bin_size)
print bins

ax = plt.gca()

# The histogram of the data
ax.hist(x, bins, color='yellow')

ax.set_xlabel('Values')
ax.set_ylabel('Frequency')

plt.ylim([0,4])
plt.show()

