#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''Avocado farmers in California wants to increase the amount of money they make. They want to know
what type of avocado to sell and where to sell it to make the most profit. To avoid higher shipping
costs and export fees, they want to keep all sales within the United States. 
    The hypotheses: Do conventional or organic avocados sell more? Where do these avocados are more
likely to sell?
    The data uses will be Avocado Prices (2020) from Kaggle.
    The data is first going to be graphed and inspected visually for normality and  skewness. Then
a t-test and a p-value will be used'''


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats


# In[3]:


PATH = r'C:\Users\charl\OneDrive\avocado-updated-2020.csv'
experiment_data = pd.read_csv(PATH)


# In[4]:


experiment_data.info()
experiment_data.head(5)


# In[5]:


# Split into two DataFrames for ease of analysis
experiment_data_conventional = experiment_data[experiment_data['type']=='conventional']
experiment_data_organic = experiment_data[experiment_data['type']=='organic']
print(experiment_data_conventional.head())
print(experiment_data_organic.head())


# In[6]:


plt.hist(experiment_data_conventional['average_price'], alpha = .5)
plt.hist(experiment_data_organic['average_price'], alpha = .5)


# In[7]:


print(stats.ttest_ind(experiment_data_conventional['average_price'], experiment_data['average_price']))
print(stats.ttest_ind(experiment_data_organic['average_price'], experiment_data['average_price']))


# In[8]:


s1 = experiment_data_conventional['average_price'].mean()
s2 = experiment_data_organic['average_price'].mean()
print('The average price for conventional avacodos is: ','$',s1 )
print('The average price for organic avacodos is: ','$',s2)


# In[9]:


experiment_data['geography'].unique()


# In[12]:


experiment_data_conventional.groupby(['geography']).mean(['average_price']) # chcecking average price for conventional by area


# In[11]:


# by inspection San Francisco appears to be selling at a very high average rate of 1.400490


# In[13]:


experiment_data_conventional.groupby(['geography']).mean(['average_price']).max() # making sure its the max


# In[14]:


experiment_data_organic.groupby(['geography']).mean(['average_price'])


# In[ ]:


# by inspection Hartford/Springfield appear to have the higest selling average price for organic avocados


# In[15]:


experiment_data_organic.groupby(['geography']).mean(['average_price']).max() #confirming the price


# In[16]:


# San Francisco isnt that far behind with price at 2.119444 
#Therefore the best place for California avocados farmers to sell their produce is in San Fransisco CA 
# organic avocados appears to be the most proffitable


# In[ ]:





# In[ ]:





# In[ ]:




