#!/usr/bin/env python
# coding: utf-8

#                         Jupyter Notebook version of the binance API learning experiments

# In[1]:


from binance.client import Client
import pprint


# In[2]:


API_KEY=""
API_SECRET=""


# In[3]:


client = Client(API_KEY, API_SECRET)
status = client.get_system_status()
info = client.get_exchange_info()


# In[5]:


pprint.pprint(status)
pprint.pprint(info)


# In[ ]:




