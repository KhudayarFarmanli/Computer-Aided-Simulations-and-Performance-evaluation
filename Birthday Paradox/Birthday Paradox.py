#!/usr/bin/env python
# coding: utf-8

# In[109]:


import numpy as np
import matplotlib.pyplot as plt
import random
import math
import scipy.stats as stats


# In[110]:


m = np.arange(10,81,10) # number of students
n = 365 # number of days in a year
q_value = 0.975     # upper limit for 95 confidence interval
runs = 100 # number of runs
exp = 5 # number of experiments


# In[112]:


# Generating random days within 365 days of the year uniformly for pre-defined number of people 
def diff_num_people(num_peop):
    exp_results = []
    for e in range(exp):   # number of experiments for calculating mean, std
        dsx = []
        for i in range(runs): # number of runs for calculating probability
            ds = []
            for j in range(num_peop): # number of people
                random.seed((e+1)*(i+1)*(j+1)) # seed for getting re-generatable results
                d = random.randint(1, n)
                ds.append(d)
            dsx.append(ds)
        exp_results.append(dsx) 

  
  """Counting the number of repetition for each element of each run of each experiment"""
    
    counts = []
    for k in range(len(exp_results)):
        for x in range(len(exp_results[k])):
            count = {item:exp_results[k][x].count(item) for item in exp_results[k][x]}
            counts.append(count) 

    return counts
    


# In[113]:


# Calculating each experiment based on written function
exp1 = diff_num_people(m[0])
exp2 = diff_num_people(m[1])
exp3 = diff_num_people(m[2])
exp4 = diff_num_people(m[3])
exp5 = diff_num_people(m[4])
exp6 = diff_num_people(m[5])
exp7 = diff_num_people(m[6])
exp8 = diff_num_people(m[7])


# In[114]:


# Separating results of each run for each experiment
l1_exp1 = exp1[:100]
l2_exp1 = exp1[100:200]
l3_exp1 = exp1[200:300]
l4_exp1 = exp1[300:400]
l5_exp1 = exp1[400:500]

l1_exp2 = exp2[:100]
l2_exp2 = exp2[100:200]
l3_exp2 = exp2[200:300]
l4_exp2 = exp2[300:400]
l5_exp2 = exp2[400:500]

l1_exp3 = exp3[:100]
l2_exp3 = exp3[100:200]
l3_exp3 = exp3[200:300]
l4_exp3 = exp3[300:400]
l5_exp3 = exp3[400:500]

l1_exp4 = exp4[:100]
l2_exp4 = exp4[100:200]
l3_exp4 = exp4[200:300]
l4_exp4 = exp4[300:400]
l5_exp4 = exp4[400:500]

l1_exp5 = exp5[:100]
l2_exp5 = exp5[100:200]
l3_exp5 = exp5[200:300]
l4_exp5 = exp5[300:400]
l5_exp5 = exp5[400:500]

l1_exp6 = exp6[:100]
l2_exp6 = exp6[100:200]
l3_exp6 = exp6[200:300]
l4_exp6 = exp6[300:400]
l5_exp6 = exp6[400:500]

l1_exp7 = exp7[:100]
l2_exp7 = exp7[100:200]
l3_exp7 = exp7[200:300]
l4_exp7 = exp7[300:400]
l5_exp7 = exp7[400:500]

l1_exp8 = exp8[:100]
l2_exp8 = exp8[100:200]
l3_exp8 = exp8[200:300]
l4_exp8 = exp8[300:400]
l5_exp8 = exp8[400:500]


# In[115]:


# Function for calculating Collision probability 
def coll(lst):
    exist = []
    for c in range(len(lst)):
        for v in range(len(list(lst[c].values()))):
            if list(lst[c].values())[v] > 1:
                exist.append(list(lst[c].values()))
                break  
        prob = len(exist)/len(lst)
    return prob


# In[116]:


# For each group of people that I have checked collision probaility, I accumulate them in the same 
# numpy array particularly to calculare mean and std easily with provided function
list_for_10s = np.array([coll(l1_exp1), coll(l2_exp1), coll(l3_exp1), coll(l4_exp1), coll(l5_exp1)])
list_for_20s = np.array([coll(l1_exp2), coll(l2_exp2), coll(l3_exp2), coll(l4_exp2), coll(l5_exp2)])
list_for_30s = np.array([coll(l1_exp3), coll(l2_exp3), coll(l3_exp3), coll(l4_exp3), coll(l5_exp3)])
list_for_40s = np.array([coll(l1_exp4), coll(l2_exp4), coll(l3_exp4), coll(l4_exp4), coll(l5_exp4)])
list_for_50s = np.array([coll(l1_exp5), coll(l2_exp5), coll(l3_exp5), coll(l4_exp5), coll(l5_exp5)])
list_for_60s = np.array([coll(l1_exp6), coll(l2_exp6), coll(l3_exp6), coll(l4_exp6), coll(l5_exp6)])
list_for_70s = np.array([coll(l1_exp7), coll(l2_exp7), coll(l3_exp7), coll(l4_exp7), coll(l5_exp7)])
list_for_80s = np.array([coll(l1_exp8), coll(l2_exp8), coll(l3_exp8), coll(l4_exp8), coll(l5_exp8)])
mean10 = list_for_10s.mean()
mean20 = list_for_20s.mean()
mean30 = list_for_30s.mean()
mean40 = list_for_40s.mean()
mean50 = list_for_50s.mean()
mean60 = list_for_60s.mean()
mean70 = list_for_70s.mean()
mean80 = list_for_80s.mean()
std10  = list_for_10s.std()
std20  = list_for_20s.std()
std30  = list_for_30s.std()
std40  = list_for_40s.std()
std50  = list_for_50s.std()
std60  = list_for_60s.std()
std70  = list_for_70s.std()
std80  = list_for_80s.std()
"""Accumulating means and stds in the same lists"""
mean_list = [mean10, mean20, mean30, mean40, mean50, mean60, mean70, mean80]
std_list = [std10, std20, std30, std40, std50, std60, std70, std80]


# In[117]:


# Calculation of Confidence Intervals of 95%
ci_list = []
for num in range(len(mean_list)):
        mean = mean_list[num]                       # Mean
        sigma = std_list[num]/math.sqrt(8)          # Standard deviation estimate
        t_value = stats.t.ppf(q = q_value, df = 7)  # Get the t-critical value
        delta = t_value * sigma                     # Margin of Error
        conf_int = [mean - delta, mean + delta]     # Calculation of Confidence Interval
        """Making sure that Confidence Interval will not be smaller than 0 and greater than 1"""
        if conf_int[0] < 0:
            conf_int[0] = 0
        if conf_int[1] > 1:
            conf_int[1] = 1
        ci_list.append(conf_int)


# In[118]:


ci_list


# In[119]:


# Visualizing Teorithical probabilitity and my obtained probabilies of Collision from simulation to see 
# how much they are overlapping

# Theorithical probability calculation
theo_prob = []
for i in range(m.shape[0]):
    prob = 1 - math.exp(-(m[i]**2)/(2*365)) # the equation for theorithical probability of collision
    theo_prob.append(prob)
    
# Separating upper and lower bounds of confidence interval for visualizing them
y_up = []
y_low = []
for j in range(len(ci_list)):
    up = ci_list[j][1]
    low = ci_list[j][0]
    y_up.append(up)
    y_low.append(low)    
      
fig, ax = plt.subplots(figsize=(8,6))
ax.fill_between(list(m), y_up, y_low, alpha=0.6, linewidth=0, label = "Confidence interval")
plt.scatter(list(m), mean_list, color = "blue" , label = "Simulation result")
plt.plot(list(m), mean_list, color = "blue", linewidth=1)
plt.scatter(list(m), theo_prob, color = "red" , label = "Theoritical result")
plt.plot(list(m), theo_prob, color = "red", linewidth=1)
plt.legend(loc = "center right")
plt.xlabel("Number of people ")
plt.ylabel("Probability of Collision")
plt.show
#fig.savefig('Relative errors', dpi=600)


# In[ ]:





# In[ ]:




