#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import hashlib
import math
from pympler import asizeof


# In[2]:


# https://datasets.imdbws.com/%C2%A0
# link to download dataset
data = pd.read_csv("title.akas.tsv", sep = "\t")


# In[3]:


# Original seem of some part of dataset
data.head(5)


# In[4]:


data.shape


# In[5]:


# I take the parts just with "IT" region
only_ita = data[data["region"] == "IT"]


# In[6]:


only_ita.head(5)


# In[7]:


# Shape of dataset contains "IT" as region
only_ita.shape


# In[8]:


# I create set from just title part
titles_set = set(only_ita["title"])


# In[9]:


# The number of elements in titles set, it is much lower than the original file with "IT" region
# the reason is set directly eliminate duplicate values
m = len(titles_set)


# In[10]:


m


# In[11]:


# Defining minimum value of B_exp by simulation in which there will be no collision in a fingerprint set
for i in range(100):
    n = 2**i         # here i = b which is bits, I start it from 0 and increase by 1 till finding minimum one
                     # in which there will be no collision
    st = set()
    for title in titles_set:
        word_hash = hashlib.md5(title.encode('utf-8')) # md5 hash
        word_hash_int = int(word_hash.hexdigest(), 16) # md5 hash in integer format
        h = word_hash_int % n  # map into [0,n-1]
        st.add(h)
        
        """I check if the filled set has the same amount of elements as original titles set"""
        
    if len(st) != m:    # If they are not equal, it means there are collisions 
        print(f"There are {m - len(st)} collisions")
    if len(st) == m:    # If they are equal the condition is met and we stop, there is no collision
        print(f"The minimum number of bits required for no collision is: {i}")
        break


# In[12]:


len(st)


# In[13]:


# For getting at most 0.5 False Positive probability we make epsilon equal to that value and 
# find the least required bits by putting it into equation
b = math.log(m/0.5, 2)


# In[14]:


round(b, 3)


# In[15]:


# Calculate the Prob(False_positive), epsilon, where bits = B_exp and see the difference
# between theoritical and experimental values
# I do this by simply putting known values into bits formula and defining epsilon as unknown
eps = round(m/(2**34), 8)


# In[16]:


# 0.00001026
eps


# In[17]:


# By using eps we again calculate B_teo to see difference with experimental one
math.log(m/eps, 2)


# In[19]:


print(f" The size of titles as python set is {asizeof.asizeof(titles_set)} bytes")
print(f" The size of titles' fingerprints as python set is {asizeof.asizeof(st)} bytes")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




