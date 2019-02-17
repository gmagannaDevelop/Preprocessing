#!/usr/bin/env python
# coding: utf-8

# # Preprocessing snippets
# Parse a JSON-lines (.jl) into a pandas DataFrame, exporting resulting tables into CSV files

# In[2]:


import pandas as pd
from Drive import Drive


# In[4]:


my_drive = Drive()
my_drive.download('journal.jl')


# In[5]:


data = pd.read_json('journal.jl', lines=True)


# In[11]:


data.head()


# In[7]:


import numpy as np


# In[9]:


bool(np.nan)


# In[ ]:




