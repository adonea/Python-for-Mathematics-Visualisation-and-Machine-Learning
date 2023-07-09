#! /usr/bin/env python3

#A Guide to Time Series Visualization with Python 3
#https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-visualization-with-python-3


import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = sm.datasets.co2.load_pandas()
co2 = data.data

print(co2.head(5))

co2.index


y = co2['co2'].resample('MS').mean()

#y.head(5)

y['1990':]

y['1995-10-01':'1996-10-01']

#Real world data tends be messy. As we can see from the plot, it is not uncommon for time-series data to contain missing values. The simplest way to check for those is either by directly plotting the data or by using the command below that will reveal missing data in ouput:

y.isnull().sum()

#Generally, we should "fill in" missing values if they are not too numerous so that we don’t have gaps in the data. We can do this in pandas using the fillna() command. For simplicity, we can fill in missing values with the closest non-null value in our time series, although it is important to note that a rolling mean would sometimes be preferable.

y = y.fillna(y.bfill())

#With missing values filled in, we can once again check to see whether any null values exist to make sure that our operation worked:

y.isnull().sum()

y.plot(figsize=(7, 6))
plt.show()

#The script below shows how to perform time-series seasonal decomposition in Python. By default, seasonal_decompose returns a figure of relatively small size, so the first two lines of this code chunk ensure that the output figure is large enough for us to visualize.

from pylab import rcParams
rcParams['figure.figsize'] =7,7

decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()
