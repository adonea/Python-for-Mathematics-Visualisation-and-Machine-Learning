
#l6_bubblecharts.py

# data from
# https://github.com/arnaudbenard/university-ranking/blob/master/timesData.csv

#Bubble Charts
#Bubble Charts Example: University world rank (first 20) vs teaching score with number of students(size) and international score (color) in 2016

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

df2016 = data[data.year == 2016].iloc[:20,:]

# information about timesData
#data.info()


# data preparation
num_students_size  = [float(each.replace(',', '.')) for each in df2016.num_students]
international_color = [float(each) for each in df2016.international]
dataNEW = [
    {
        'y': df2016.teaching,
        'x': df2016.world_rank,
        'mode': 'markers',
        'marker': {
            'color': international_color,
            'size': num_students_size,
            'showscale': True
        },
        "text" :  df2016.university_name    
    }
]

  
py.plot(dataNEW)
