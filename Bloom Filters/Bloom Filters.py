#!/usr/bin/env python
# coding: utf-8

# In[3]:


import hashlib
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[4]:


# https://datasets.imdbws.com/%C2%A0
# link to download dataset
data = pd.read_csv("title.akas.tsv", sep = "\t")
# I take the parts just with "IT" region
only_ita = data[data["region"] == "IT"]
# I create set from just title part
titles_set = set(only_ita["title"])


# In[5]:


# The number of elements in titles set, it is much lower than the original file with "IT" region
# the reason is set directly eliminate duplicate values
m = len(titles_set)
m


# In[6]:


# The number of bits considered for testing
bits = np.arange(19, 24, 1)
print(bits)


# In[7]:


# K value for defining optimal number of hash functions based on number of bits calculated as below
k_opts = []
for b in bits:
    n = 2**b
    k_opt = round((n/m)*math.log(2))
    k_opts.append(k_opt)


# In[8]:


k_opts


# In[9]:


def compute_all_hashes(md5, num_hashes, b):
    # returns the list of num_hashes indexes corresponding to all the bits to update in a bloom filter
    # md5 is the hash integer value obtained by md5, on 128 bits
    # num_hashes is the number of hash values to generate
    # b is the number of bits such that the bit array is of size 2**b
    debug=True # flag to obtain debug info, useful to understand how the function work
    bits_to_update=[] # the list of bits to update is initially empty
    if (b+3*num_hashes>128): # check the condition about the max number of supported hashes
        print("Error - at most 32 hashes")
        return -1
    for i in range(num_hashes): # for each hash to generate
        if debug:
            print("{0:b}".format(md5)) # print the md5 value in binary
        value=md5 % (2 ** b) # take the last b bits for the hash value
        bits_to_update.append(value) # add the hash value in the list
        if debug:
            print("Hash value:",value,"\t{0:b}".format(value)) # debug
        md5 = md5 // (2 ** 3) # right-shift the md5 by 3 bits
    return bits_to_update


# In[10]:


# Function for calculating Bloom Filters
def hashes_bits(k, b):
    lst = []
    for title in titles_set:
        word_hash = hashlib.md5(title.encode('utf-8')) # md5 hash
        word_hash_int = int(word_hash.hexdigest(), 16) # md5 hash in integer format
        all_bits_to_update=compute_all_hashes(word_hash_int, k, b)#k_opts[0], bits[0])
        lst.append(all_bits_to_update)
        
#It provides array where the particular index filled with 1 bit 
#if index number is presented in bloom filters at least once
    my_arr = np.zeros(2**b)
    flatten_list = list(np.concatenate(lst).flat)
    for el in flatten_list:
        my_arr[el] = 1

#It calculates at the end how many 1 bits we get for each number of bits
    count = 0
    for i in range(my_arr.shape[0]):
        if my_arr[i] == 1:
            count = count + 1
      
    return count


# In[ ]:


#Getting results of function
bits_19_count = hashes_bits(k_opts[0], bits[0])
bits_20_count = hashes_bits(k_opts[1], bits[1])
bits_21_count = hashes_bits(k_opts[2], bits[2])
bits_22_count = hashes_bits(k_opts[3], bits[3])
bits_23_count = hashes_bits(int(k_opts[4]), int(bits[4])) 


# In[ ]:


# Storing results into list and printing
l_bits = [bits_19_count, bits_20_count, bits_21_count, bits_22_count, bits_23_count]
print(bits_19_count)
print(bits_20_count)
print(bits_21_count)
print(bits_22_count)
print(bits_23_count)


# In[ ]:


# Calculating False Positive Probability for both Empirical and Theoritical results
empirical = []
theoritical = []
for i in range(len(l_bits)):
    emp = (l_bits[i]/2**bits[i])**k_opts[i]
    empirical.append(emp)
    theo = (1 - math.pow(math.e, (-k_opts[i]*m)/2**bits[i]))**k_opts[i]
    theoritical.append(theo)


# In[ ]:


print(empirical)
print(theoritical)


# In[ ]:


# Visualizing False Positive probability for Bloom filters based on Empirical results

fig = plt.subplots(figsize=(8,6))
plt.scatter(bits, empirical, color = "blue" )
plt.plot(bits, empirical, color = "blue", linewidth=2)

plt.xlabel("Number of Bits")
plt.ylabel("Probability of False positive")
plt.show()


# In[ ]:


# Visualizing False Positive probability for Bloom filters based on Theoritical results

fig = plt.subplots(figsize=(8,6))
plt.scatter(bits, theoritical, color = "red" )
plt.plot(bits, theoritical, color = "red", linewidth=2)

plt.xlabel("Number of Bits")
plt.ylabel("Probability of False positive")
plt.show()


# In[ ]:


# Calculation of False Positive based on defined bits for Fingerprinting which directly can be applied with formula
Pr = []
for j in bits:
    fp = m/2**j
    Pr.append(fp)


# In[ ]:


# Generating Bit string based on defined bits
bts_list = []
for b in bits:
    n = 2**b   
    lstr = []
    for title in titles_set:
        word_hash = hashlib.md5(title.encode('utf-8')) # md5 hash
        word_hash_int = int(word_hash.hexdigest(), 16) # md5 hash in integer format
        h = word_hash_int % n  # map into [0,n-1]
        lstr.append(h)
        
    new_list = []
    for i in range(len(lstr)):
        if i == 0:
            new_list.append(1)
            continue
        if lstr[i] not in lstr[:(i-1)]:
            new_list.append(1)
        else:
            new_list.append(0)
    bts_list.append(new_list)


# In[ ]:


# Calculating False Positive probability of Bit String arrays for each particular bit group empirically
fp_19 = len(bts_list[0])/(2**bits[0])
fp_20 = len(bts_list[1])/(2**bits[1])
fp_21 = len(bts_list[2])/(2**bits[2])
fp_22 = len(bts_list[3])/(2**bits[3])
fp_23 = len(bts_list[4])/(2**bits[4])


# In[ ]:


# Storing them into a list and printing
fp_bts_list = [fp_19, fp_20, fp_21, fp_22, fp_23] 
print(fp_19)
print(fp_20)
print(fp_21)
print(fp_22)
print(fp_23)


# In[ ]:


# Visualizing False Positive probability for Bloom filters based on Empirical results

fig = plt.subplots(figsize=(8,6))
plt.scatter(bits, empirical, color = "blue", label = "Bloom Filters results")
plt.plot(bits, empirical, color = "blue", linewidth=2)

plt.scatter(bits, Pr, color = "green", label = "Fingerprinting results")
plt.plot(bits, Pr, color = "green", linewidth=2)

plt.scatter(bits, fp_bts_list, color = "orange", label = "Bit strings results")
plt.plot(bits, fp_bts_list, color = "orange", linewidth=2)
plt.legend(loc = "upper right")
plt.xlabel("Number of Bits")
plt.ylabel("Probability of False positive")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




