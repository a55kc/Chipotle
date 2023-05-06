#!/usr/bin/env python
# coding: utf-8

# # LOAD THE DATASET FROM THE GIVEN BELOW LINK.

# https://drive.google.com/file/d/1RWvyhf9AcDZsSB5xVVgzsbHI1m4sFBJf/view?usp=share_link

# In[3]:


import pandas as pd


# In[4]:


df =  pd.read_csv(r'C:\Users\acer\Desktop\chipotle - chipotle.csv')


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.describe()


# # USING PANDAS FUNCTION CALCULATE HOW MANY PRODUCTS COSTS MORE THAN $10?

# In[8]:


df.info()


# In[9]:


df['cost']=pd.to_numeric(df.item_price.str.slice(1))


# In[10]:


df['price_per_item']=df.cost/df.quantity


# In[11]:


product_prices=df.groupby('item_name').agg({'price_per_item':'max'})


# In[12]:


(product_prices.price_per_item>10).sum() # PRODUCTS COSTS MORE THAN $10


# 
# # What is the price of each item?

# In[13]:


df['cost']=pd.to_numeric(df.item_price.str.slice(1))
df['price_per_item']=df.cost/df.quantity
product_prices=df.groupby('item_name').agg({'price_per_item':'max'})


# In[14]:


product_prices


# # Which is the Most Expensive Item?

# In[18]:


df.cost.idxmax()


# In[19]:


df.loc[3598,:]


# In[ ]:





# In[ ]:




