#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import  statsmodels.api as sm
import statsmodels.stats.api as sms
from scipy.stats import boxcox


# In[2]:


covid_1 =pd.read_csv("/Users/arkajiad/Downloads/Covid Vaccine Datasets only/covid19vaccinesbycounty.csv")


# In[5]:


sns.distplot(covid_1['jj_doses'])


# In[6]:


sns.distplot(covid_1['pfizer_doses'])


# In[7]:


sns.distplot(covid_1['moderna_doses'])


# In[9]:


x = covid_1['jj_doses']
y = covid_1['moderna_doses']


# In[10]:


c1 = sm.OLS(y,x).fit()


# In[11]:


pred_val = c1.fittedvalues.copy()
true_val = covid_1['jj_doses'].values.copy()
residual = true_val - pred_val


# In[12]:


fig, ax = plt.subplots(figsize=(6, 2.5))
_ = ax.scatter(residual, pred_val)


# In[13]:


sms.diagnostic.het_breuschpagan(residual, covid_1[['moderna_doses']])


# In[17]:


covid_1.corr()


# In[18]:


sns.heatmap(covid_1.corr(), annot=True)


# In[22]:


fig, ax = plt.subplots(figsize=(12,8))
fig = sm.graphics.influence_plot(c1, alpha = .05, ax = ax, criterion="cooks")


# In[23]:


c1.summary()


# In[ ]:





# In[ ]:





# In[ ]:




