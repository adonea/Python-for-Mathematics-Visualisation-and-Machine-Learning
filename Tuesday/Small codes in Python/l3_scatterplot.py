
#l3_scatterplot.py

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
df2014 = data[data.year == 2014].iloc[:100,:]
df2015 = data[data.year == 2015].iloc[:100,:]
df2016 = data[data.year == 2016].iloc[:100,:]
# import graph objects as "go"
import plotly.graph_objs as go


# creating trace1
trace1 =go.Scatter(
                    x = df2014.world_rank,
                    y = df2014.citations,
                    mode = "markers",
                    name = "2014",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= df2014.university_name)
# creating trace2
trace2 =go.Scatter(
                    x = df2015.world_rank,
                    y = df2015.citations,
                    mode = "markers",
                    name = "2015",
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text= df2015.university_name)
# creating trace3
trace3 =go.Scatter(
                    x = df2016.world_rank,
                    y = df2016.citations,
                    mode = "markers",
                    name = "2016",
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text= df2016.university_name)
data = [trace1, trace2, trace3]
layout = dict(title = 'Citation vs world rank of top 100 universities with 2014, 2015 and 2016 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Citation',ticklen= 5,zeroline= False)
             )
fig = dict(data = data, layout = layout)

py.plot(fig)

