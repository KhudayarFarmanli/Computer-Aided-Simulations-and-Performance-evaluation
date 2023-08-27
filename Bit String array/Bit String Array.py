#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import math
import hashlib
import matplotlib.pyplot as plt
import copy
from pympler import asizeof


# In[2]:


# https://datasets.imdbws.com/%C2%A0
# link to download dataset
data = pd.read_csv("title.akas.tsv", sep = "\t")


# In[3]:


# I take the parts just with "IT" region
only_ita = data[data["region"] == "IT"]


# In[4]:


# I create set from just title part
titles_set = set(only_ita["title"])


# In[5]:


# The number of elements in titles set, it is much lower than the original file with "IT" region
# the reason is set directly eliminate duplicate values
m = len(titles_set)


# In[6]:


m


# In[7]:


# The number of bits considered for testing
bits = np.arange(19, 27, 1)
print(bits)


# In[8]:


# Function to calculate fingerprints for different number of bits

def num_bits(b):
    n = 2**b         
    st = set()
    for title in titles_set:
        word_hash = hashlib.md5(title.encode('utf-8')) # md5 hash
        word_hash_int = int(word_hash.hexdigest(), 16) # md5 hash in integer format
        h = word_hash_int % n  # map into [0,n-1]
        st.add(h)
    return st


# In[9]:


# Fingerprint set of different number of bits

num_19 = num_bits(bits[0])
num_20 = num_bits(bits[1])
num_21 = num_bits(bits[2])
num_22 = num_bits(bits[3])
num_23 = num_bits(bits[4])
num_24 = num_bits(bits[5])
num_25 = num_bits(bits[6])
num_26 = num_bits(bits[7])


# In[10]:


# Creating Bit string arrays based on particular number of bits

def bit_string(b):
    n = 2**b   
    #BA = np.ones(m)
    lst = []
    for title in titles_set:
        word_hash = hashlib.md5(title.encode('utf-8')) # md5 hash
        word_hash_int = int(word_hash.hexdigest(), 16) # md5 hash in integer format
        h = word_hash_int % n  # map into [0,n-1]
        lst.append(h)
        
    new_list = []
    for i in range(len(lst)):
        if i == 0:
            new_list.append(1)
            continue
        if lst[i] not in lst[:(i-1)]:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list


# In[11]:


# Number of bits calculated for each group

one_zeros_19 = bit_string(bits[0])
one_zeros_20 = bit_string(bits[1])
one_zeros_21 = bit_string(bits[2])
one_zeros_22 = bit_string(bits[3])
one_zeros_23 = bit_string(bits[4])
one_zeros_24 = bit_string(bits[5])
one_zeros_25 = bit_string(bits[6])
one_zeros_26 = bit_string(bits[7])


# In[14]:


# Gathering them into one list
list_one_zeros = [one_zeros_19,one_zeros_20,one_zeros_21,one_zeros_22,one_zeros_23,one_zeros_24,one_zeros_25, one_zeros_26]


# In[15]:


# Calculating False Positive probability of Bit String arrays for each particular bit group theoritically

fp_19 = len(num_19)/(2**bits[0])
fp_20 = len(num_20)/(2**bits[1])
fp_21 = len(num_21)/(2**bits[2])
fp_22 = len(num_22)/(2**bits[3])
fp_23 = len(num_23)/(2**bits[4])
fp_24 = len(num_24)/(2**bits[5])
fp_25 = len(num_25)/(2**bits[6])
fp_26 = len(num_26)/(2**bits[7])


# In[16]:


print(fp_19)
print(fp_20)
print(fp_21)
print(fp_22)
print(fp_23)
print(fp_24)
print(fp_25)
print(fp_26)


# In[31]:


# Visualizing how changing number of bits affect the probability of false positive for bit string array
prob_list = [fp_19, fp_20, fp_21, fp_22, fp_23, fp_24, fp_25, fp_26]


fig = plt.subplots(figsize=(8,6))
plt.scatter(bits, prob_list, color = "blue" )
plt.plot(bits, prob_list, color = "blue", linewidth=2)

plt.xlabel("Number of Bits")
plt.ylabel("Probability of False positive")
plt.show()


# In[18]:


# Calculating False Positive probability of Fingerprint sets for each particular bit group theoritically

fp_19_finger = 1 - (1- (1/(2**bits[0])))**m
fp_20_finger = 1 - (1- (1/(2**bits[1])))**m
fp_21_finger = 1 - (1- (1/(2**bits[2])))**m
fp_22_finger = 1 - (1- (1/(2**bits[3])))**m
fp_23_finger = 1 - (1- (1/(2**bits[4])))**m
fp_24_finger = 1 - (1- (1/(2**bits[5])))**m
fp_25_finger = 1 - (1- (1/(2**bits[6])))**m
fp_26_finger = 1 - (1- (1/(2**bits[7])))**m


# In[19]:


print(fp_19_finger)
print(fp_20_finger)
print(fp_21_finger)
print(fp_22_finger)
print(fp_23_finger)
print(fp_24_finger)
print(fp_25_finger)
print(fp_26_finger)


# In[20]:


# Visualizing how changing number of bits affect the probability of false positive for fingerprinting
prob_list_finger = [fp_19_finger, fp_20_finger, fp_21_finger, fp_22_finger, fp_23_finger, fp_24_finger, fp_25_finger, fp_26_finger] 

fig = plt.subplots(figsize=(8,6))

plt.scatter(bits, prob_list_finger, color = "red" )
plt.plot(bits, prob_list_finger, color = "red", linewidth=2)

plt.xlabel("Number of Bits")
plt.ylabel("Probability of False positive")
plt.show()


# In[23]:


# Calculating size of Bit string arrays, since they are equal we can assign one for further calculation
size_bit = asizeof.asizeof(one_zeros_19)
asizeof.asizeof(one_zeros_19)


# In[22]:


size_bit


# In[24]:


# Calculating size of each bit group of Fingerprint sets

size_fing_19 = asizeof.asizeof(num_19)
size_fing_20 = asizeof.asizeof(num_20)
size_fing_21 = asizeof.asizeof(num_21)
size_fing_22 = asizeof.asizeof(num_22)
size_fing_23 = asizeof.asizeof(num_23)
size_fing_24 = asizeof.asizeof(num_24)
size_fing_25 = asizeof.asizeof(num_25)
size_fing_26 = asizeof.asizeof(num_26)


# In[25]:


print(size_fing_19)
print(size_fing_20)
print(size_fing_21)
print(size_fing_22)
print(size_fing_23)
print(size_fing_24)
print(size_fing_25)
print(size_fing_26)


# In[26]:


fing_list = [size_fing_19, size_fing_20, size_fing_21, size_fing_22, size_fing_23, size_fing_24, size_fing_25, size_fing_26]


# In[28]:


# Plotting memory taken by both Fingerprint sets and Bit string arrays to see difference

fig = plt.subplots(figsize=(8,6))

plt.bar(bits + 0.2, fing_list, width = 0.3, label = "Fingerprint")
plt.bar(bits - 0.2, size_bit, width = 0.3, label = "Bit string")

plt.legend(loc = "upper left")
plt.xlabel("Number of Bits")
plt.ylabel("Memory taken in bytes")

