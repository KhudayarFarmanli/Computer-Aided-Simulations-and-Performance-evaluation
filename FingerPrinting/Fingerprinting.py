#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import math
from pympler import asizeof    # for getting size of file


# In[2]:


# Reading dictionary from txt file as python set
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt    <-------------- link to dataset
words =  set(open('words_alpha.txt').read().split())


# In[3]:


# The number of words available in the file
m = len(words)


# In[4]:


m


# In[5]:


# Defining minimum value of B_exp by simulation in which there will be no collision in a fingerprint set
for i in range(100):
    n = 2**i         # here i = b which is bits, I start it from 0 and increase by 1 till finding minimum one
                     # in which there will be no collision
    st = set()
    for word in words:
        word_hash = hashlib.md5(word.encode('utf-8')) # md5 hash
        word_hash_int = int(word_hash.hexdigest(), 16) # md5 hash in integer format
        h = word_hash_int % n  # map into [0,n-1]
        st.add(h)
        
        """I check if the filled set has the same amount of elements as original dictionary set"""
        
    if len(st) != m:    # If they are not equal, it means there are collisions 
        print(f"There are {m - len(st)} collisions")
    if len(st) == m:    # If they are equal the condition is met and we stop, there is no collision
        print(f"The minimum number of bits required for no collision is: {i}")
        break


# In[6]:


len(st)


# In[7]:


# For getting at most 0.5 False Positive probability we make epsilon equal to that value and 
# find the least required bits by putting it into equation
b = math.log(m/0.5, 2)


# In[8]:


round(b, 3)


# In[9]:


# Calculate the Prob(False_positive), epsilon, where bits = B_exp and see the difference
# between theoritical and experimental values
# I do this by simply putting known values into bits formula and defining epsilon as unknown
eps = round(m/(2**39), 10)


# In[10]:


# 0.0000006732
eps


# In[11]:


# By using eps we again calculate B_teo to see difference with experimental one
math.log(m/eps, 2)


# In[12]:


print(f" The size of dictionary of distinct words as python set is {asizeof.asizeof(words)} bytes")
print(f" The size of Fingerprints as python set is {asizeof.asizeof(st)} bytes")


# In[ ]:





# In[ ]:




