#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages


# In[2]:


import pandas as pd
import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy import stats
from scipy.stats import ttest_ind 
import matplotlib.pyplot as plt 
import seaborn as sns
import openpyxl


# In[3]:


# QUESTIONS
#3.	Does the vaccination rate decrease after the California stay-at-home was lifted (June 15, 2021) compare after 30, 60, and 90 days?
#4.	Does the vaccination rate decrease after the California stay-at-home was lifted (June 15, 2021) compared to the 4 largest counties?
#*SIDE NOTE: Comparre the Vaccine Rate for the 4 largest counties in NV & TX


# In[4]:


covid_19 =pd.read_csv("/Users/arkajiad/Downloads/Covid Vaccine Datasets only/covid19vaccinesbycounty.csv")


# In[5]:


covid_19.head()


# In[6]:


covid_19.tail()


# In[7]:


#summary of covid


# In[8]:


covid_19.isnull().sum()


# In[9]:


covid_19.value_counts()


# In[10]:


covid_19.dropna(inplace=True)


# In[11]:


covid_19.head(5)


# In[12]:


covid_199 = covid_19.drop(['booster_recip_count', 'cumulative_booster_recip_count', 'cumulative_at_least_one_dose', 'at_least_one_dose',
                           'cumulative_fully_vaccinated', 'partially_vaccinated', 'cumulative_jj_doses',
                          'cumulative_pfizer_doses', 'cumulative_moderna_doses', ], axis=1)


# In[13]:


covid_199.head(5)


# In[14]:


covid_199['pfizer_doses'].hist()


# In[15]:


covid_199.hist()


# In[16]:


covid_199.head()


# In[17]:


covid_199.mean()


# In[18]:


covid_199.min()


# In[19]:


covid_199.std()


# In[20]:


covid_199['county'].hist()


# In[21]:


covid_199.value_counts("california_flag")


# In[ ]:


def recode (series):
  if series == "california_flag":
    return "california"
  if series == "OG column category": 
    return "1"
  if series == "OG column category"": 
    return "2"
  if series == "OG column category"": 
    return "3"
DataSetName["RecodeColName] = DataSetName["OriginalColName"].apply(NewFunctionName )


# In[21]:


covid_19 = california_flag.column.astype(int)


# In[22]:





# In[22]:


covid_199.drop(covid_199.index[covid_199['california_flag'] == 'Not in California'], inplace=True)


# In[23]:


print(covid_199)


# In[24]:


covid_199.value_counts("california_flag")


# In[25]:


covid_199.mean()


# In[26]:


covid_199.mode()


# In[27]:


covid_199.median()


# In[28]:


covid_199.hist()


# In[29]:


pd.options.display.max_rows = None


# In[30]:


covid_199.columns


# In[32]:


covid_199.value_counts()


# In[33]:


covid_199.corr(method='pearson')


# In[34]:


covid_199.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)


# In[35]:


sns.pairplot(covid_199)


# In[36]:


sns.displot(covid_199['pfizer_doses'])


# In[37]:


sns.displot(covid_199['jj_doses'])


# In[38]:


str(covid_199)


# In[39]:


covid_199.info()


# In[40]:





# In[41]:


nv_c.head()


# In[43]:


covid_199.groupby('county')[jj_doses].max()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




