
#l4_barcharts.py

# data from
# https://github.com/arnaudbenard/university-ranking/blob/master/timesData.csv


import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

import plotly.plotly as py
import plotly.figure_factory

# generated at https://plot.ly/settings/api
py.sign_in('adonea','2i7tqPLIVD6kI9nJ3EFM')

#Let us import a dataset to perform our statistics. We will be looking at the consumption of alcohol by country in 2010.

data = pd.read_csv('timesData.csv')

# information about timesData
#data.info()


# prepare data frames
df2014 = data[data.year == 2014].iloc[:3,:]
#request information:
#df2014


# import graph objects as "go"
import plotly.graph_objs as go
# create trace1 
trace1 = go.Bar(
                x = df2014.university_name,
                y = df2014.citations,
                name = "citations",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
# create trace2 
trace2 = go.Bar(
                x = df2014.university_name,
                y = df2014.teaching,
                name = "teaching",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
data = [trace1, trace2]
layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
py.plot(fig)
