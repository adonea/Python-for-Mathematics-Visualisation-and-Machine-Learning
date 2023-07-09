
#l5_piechart.py

# data from
# https://github.com/arnaudbenard/university-ranking/blob/master/timesData.csv

#Pie Charts Example: Students rate of top 7 universities in 2016

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


# data preparation
df2016 = data[data.year == 2016].iloc[:7,:]
pie1 = df2016.num_students
pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  # str(2,4) => str(2.4) = > float(2.4) = 2.4
labels = df2016.university_name
# figure
fig = {
  "data": [
    {
      "values": pie1_list,
      "labels": labels,
      "domain": {"x": [0, .5]},
      "name": "Number Of Students Rates",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
  "layout": {
        "title":"Universities Number of Students rates",
        "annotations": [
            { "font": { "size": 20},
              "showarrow": False,
              "text": "Number of Students",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}
py.plot(fig)
