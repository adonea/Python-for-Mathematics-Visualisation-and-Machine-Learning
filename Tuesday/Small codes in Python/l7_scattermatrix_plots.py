
#l7_scatter matrix plot.py

#Scatter Matrix Plots
#Scatter Matrix = it helps us to see covariance and relation between more than 2 features

# 
#import figure factory as ff
#create_scatterplotmatrix = creates scatter plot
#data2015 = prepared data. It includes research, international and total scores with index from 1 to 401
#colormap = color map of scatter plot
#colormap_type = color type of scatter plot
#height and weight

# data from
# https://github.com/arnaudbenard/university-ranking/blob/master/timesData.csv

import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

import plotly.plotly as py
import plotly.figure_factory as ff

# generated at https://plot.ly/settings/api
py.sign_in('adonea','2i7tqPLIVD6kI9nJ3EFM')

#Let us import a dataset to perform our statistics. We will be looking at the consumption of alcohol by country in 2010.

data = pd.read_csv('timesData.csv')

# prepare data
dataframe = data[data.year == 2015]
data2015 = dataframe.loc[:,["research","international", "total_score"]]
data2015["index"] = np.arange(1,len(data2015)+1)
# scatter matrix
fig = ff.create_scatterplotmatrix(data2015, diag='box', index='index',colormap='Portland',
                                  colormap_type='cat',
                                  height=700, width=700)
  
py.plot(fig)
