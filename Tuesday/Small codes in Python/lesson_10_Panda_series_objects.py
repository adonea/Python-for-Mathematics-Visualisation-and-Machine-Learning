
# coding: utf-8

#  Pandas;
# 
# It contains high-level data structures and manipulation tools designed to make data analysis fast and easy in Python. pandas is built on top of NumPy and makes it easy to use in NumPy-centric applications.

# # PART1 Data Structures 

# To get started with pandas, you will need to get comfortable with its two workhorse data structures: Series and DataFrame. While they are not a universal solution for every problem, they provide a solid, easy-to-use basis for most applications.
# 

# # Series

# A Series is a one-dimensional array-like object containing an array of data (of any NumPy data type) and an associated array of data labels, called its index. The simplest Series is formed from only an array of data:

#!!!!!!!!!!!!!!!!!!!!!!!!!!
# MUST PRINT out your outputs


# In[8]:

import numpy as np

from pandas import Series, DataFrame


# In[9]:


import pandas as pd


# In[23]:


obj = Series([4, 7, -5, 3])


# In[24]:


obj


# In[28]:


obj.values


# In[29]:


obj.index


# Often it will be desirable to create a Series with an index identifying each data point:

# In[26]:


obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])


# In[27]:


obj2


# In[16]:


obj2.index


# In[30]:


obj2['a']


# Change an element: 

# In[31]:


obj2['d'] = 6


# In[32]:


obj2[['c', 'a', 'd']]


# In[33]:


obj2


# filtering with a boolean array, scalar multiplication, or applying math functions, will preserve the index-value link:

# In[34]:


obj2[obj2 > 0]


# In[35]:


obj2 * 2


# In[36]:


np.exp(obj2)


# New data: create a series

# In[17]:


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}


# In[18]:


obj3 = Series(sdata)


# In[19]:


obj3


# # DataFrame

# A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.).

# In[20]:


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)


# The resulting DataFrame will have its index assigned automatically as with Series, and the columns are placed in sorted order:

# In[21]:


frame


# Order of columns is specified:

# In[37]:


DataFrame(data, columns=['year', 'state', 'pop'])


# As with Series, if you pass a column that isn’t contained in data, it will appear with NA values in the result:

# In[39]:


frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], 
                   index=['one', 'two', 'three', 'four', 'five'])


# In[40]:


frame2


# Another common form of data is a nested dict of dicts format:

# In[41]:


pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}


# In[42]:


frame3 = DataFrame(pop)


# In[43]:


frame3


# # Handling Missing Data

# Missing data is common in most data analysis applications. One of the goals in de- signing pandas was to make working with missing data as painless as possible. 

# In[44]:


string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])


# In[45]:


string_data


# pandas uses the floating point value NaN (Not a Number) to represent missing data in both floating as well as in non-floating point arrays. It is just used as a sentinel that can be easily detected:

# # Filtering Out Missing Data

# You have a number of options for filtering out missing data. While doing it by hand is always an option, dropna can be very helpful. On a Series, it returns the Series with only the non-null data and index values:

# In[46]:


from numpy import nan as NA


# In[47]:


data = Series([1, NA, 3.5, NA, 7])


# In[48]:


data.dropna()


# Naturally, you could have computed this yourself by boolean indexing:

# In[50]:


data[data.notnull()]


# With DataFrame objects, these are a bit more complex. You may want to drop rows or columns which are all NA or just those containing any NAs. 

# In[52]:


data = DataFrame([[1., 6.5, 3.], [1., NA, NA], 
                  [NA, NA, NA], [NA, 6.5, 3.]])


# dropna by default drops any row containing a missing value:

# In[53]:


cleaned = data.dropna()


# In[55]:


data


# In[56]:


cleaned


# Passing how='all' will only drop rows that are all NA:

# In[57]:


data.dropna(how='all')


# Dropping columns in the same way is only a matter of passing axis=1:
# 
# Generate a column:

# In[60]:


data[4]=NA


# In[61]:


data


# In[59]:


data.dropna(axis=1, how='all')


# A related way to filter out DataFrame rows tends to concern time series data. Suppose you want to keep only rows containing a certain number of observations. You can indicate this with the thresh argument:

# In[62]:


df = DataFrame(np.random.randn(7, 3))


# In[64]:


df.ix[:4, 1] = NA; df.ix[:2, 2] = NA


# In[65]:


df


# In[66]:


df.dropna(thresh=3)


# # Filling in Missing Data

# Rather than filtering out missing data (and potentially discarding other data along with it), you may want to fill in the “holes” in any number of ways. For most purposes, the fillna method is the workhorse function to use. Calling fillna with a constant replaces missing values with that value:

# In[67]:


df.fillna(0)


# In[68]:


df.fillna({1: 0.5, 3: -1})


# fillna returns a new object

# In[ ]:




