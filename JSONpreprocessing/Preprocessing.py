#!/usr/bin/env python
# coding: utf-8

# # Preprocessing snippets
# Parse a JSON-lines (.jl) into a pandas DataFrame, exporting resulting tables into CSV files

# In[60]:


import json
import pandas as pd
from Drive import Drive


# In[2]:


my_drive = Drive()
my_drive.download('journal.jl')


# In[54]:


data = pd.read_json('journal.jl', lines=True)
data.head()


# In[ ]:





# In[72]:


def list_to_string(ls: list) -> str:
    _str = ''
    for val in ls:
        _str += f'{val.strip()} '
    _str = _str.strip()
    return _str


# In[73]:


x = list_to_string(['hola', 'como'])


# In[74]:


with open('journal.jl', 'r') as fsock1, open('journal2.jl', 'a') as fsock2:
    for line in fsock1:
        _tmp = json.loads(line)
        #print(_tmp['food'])
        if 'food' in _tmp.keys():
            _tmp['food'] = (lambda x: list_to_string(x) if x else None)(_tmp['food'])
            #print(_tmp['food'])
            fsock2.write(f'{json.dumps(_tmp)}\n')


# In[58]:


"""data['food'] = pd.core.series.Series(
                map(
                    lambda x: list_to_string(x) if x else None, data['food']
                    )
                )
"""
type(data['food'])


# In[75]:


data2 = pd.read_json('journal2.jl', lines=True)
data2['food'][166]


# In[18]:


type(data['food'])


# In[6]:


pd.core.series.Series([1, 2, 3])


# In[9]:





# In[ ]:




