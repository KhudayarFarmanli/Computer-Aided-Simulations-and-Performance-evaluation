#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math 
import random
import scipy.stats as stats


# In[2]:


num_exp = 15
means = []
conf_ints = [] 
accuracies = []


# In[3]:


q_value = [0.95, 0.975, 0.995]                        # 90, 95, 99 Confidence intervals upper limits particularly
length = len(q_value)
for i in range(length):
    np.random.seed(8111996)                           # Generating Seed
    for exp in range(num_exp):
        sample = np.random.uniform(0, 10, 30)         # Generating Sample of 30 values Uniformly between 0 and 10
        mean = sample.mean()                          # Calculating Sample mean
        means.append(mean)
        std = sample.std(ddof = 1)                    # Calculating Sample Std with 1 degrees of freedom
        sigma = std/math.sqrt(sample.size)            # Standard deviation estimate
        t_value = stats.t.ppf(q = q_value[i], df=29)  # Get the t-critical value
        delta = t_value * sigma                       # Margin of Error
        conf_int = (mean - delta, mean + delta)       # Calculation of Confidence Interval
        conf_ints.append(conf_int)
        
        relative_error = delta/mean                   # Calculation of Relative Error
        accuracy = 1 - relative_error                 # Calculation of Accuracy
        accuracies.append(accuracy)


# In[4]:


len(conf_ints)


# In[5]:


means = means[:15]
conf_ints_90 = conf_ints[:15]
conf_ints_95 = conf_ints[15:30]
conf_ints_99 = conf_ints[30:45]
accuracies_90 = accuracies[:15]
accuracies_95 = accuracies[15:30]
accuracies_99 = accuracies[30:45]


# In[6]:


# Visualizing Confidence Intervals
conf_ints_list = [conf_ints_90, conf_ints_95, conf_ints_99]

for i in range(len(conf_ints_list)):
    plt.figure(figsize=(8,6))
    plt.xlabel("Experiments")
    plt.ylabel("Confidence Interval")
    plt.errorbar(x=np.arange(0, 15, 1), y=means, yerr=[(up-down)/2 for up,down in conf_ints_list[i]], fmt='o')


# In[7]:


# Visualizing Accuracies based on particular Confidence Intervals
accuracy_list = [accuracies_90, accuracies_95, accuracies_99]

for i in range(len(accuracy_list)):
    plt.figure(figsize=(8,6))
    plt.plot(accuracy_list[i])
    plt.xlabel("Experiments")
    plt.ylabel("Accuracy")
    plt.show()  


# In[ ]:




