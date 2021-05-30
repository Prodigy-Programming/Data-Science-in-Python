#!/usr/bin/env python
# coding: utf-8

# In[25]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


df=sns.load_dataset("iris")


# In[ ]:





# In[34]:


df.head()


# In[36]:


df.shape


# In[38]:


#univariate analysis:


# In[39]:


df_setosa=df.loc[df["species"]=="setosa"]


# In[43]:


df_virginica=df.loc[df["species"]=="virginica"]
df_versicolor=df.loc[df["species"]=="versicolor"]


# In[52]:


plt.plot(df_setosa["sepal_length"],np.zeros_like(df_setosa["sepal_length"]),'*')
plt.plot(df_virginica["sepal_length"],np.zeros_like(df_virginica["sepal_length"]),"o")
plt.plot(df_versicolor["sepal_length"],np.zeros_like(df_versicolor["sepal_length"]),">")
plt.show()


# In[53]:


# bivariate analysis


# In[59]:


sns.scatterplot("petal_length","petal_width",data=df,hue="species")


# In[60]:


# multivariate


# In[62]:


sns.pairplot(df,hue="species")


# In[ ]:




