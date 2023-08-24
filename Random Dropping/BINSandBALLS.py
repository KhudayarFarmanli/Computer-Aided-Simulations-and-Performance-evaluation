#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 
import math
import random
import copy
import scipy.stats as stats


# In[2]:


# Here I define the number of Bins and Balls along number of experiments and confidence interval
bins_balls = [10,20,30,40,50]
num_exp = 15
ci = 0.95


# In[3]:


# I create list of lists for empty Bins and numpy array for Balls which contain only ones to fill bins later
balls = []
bins = []
for i in range(len(bins_balls)):
    ball_pack = np.ones(bins_balls[i])
    balls.append(ball_pack)
    bin_lists = [[] for i in range(balls[i].shape[0])]
    bins.append(bin_lists)


# In[4]:


# I am filling bins with balls based on given condition 'k' number of random bins picked to throw the ball
# Also doing same experiments repeatedly based on pre-defined given number of experiments
bins_new = [] # I fill experiment results here by appending
for exp in range(num_exp):
    random.seed(exp+1)
    bins_copied = copy.deepcopy(bins)
    for pack in range(len(balls)):
        for ball in range(balls[pack].shape[0]):
            selected = random.choices(bins_copied[pack], k = 1)  #pick random k number of bins uniformly with replacement
            min(selected, key=len).append(balls[pack][ball])  # place the ball to the least occupied one
    bins_new.append(bins_copied)


# In[5]:


bins_new[14][0]


# In[6]:


# After accumulation of single balls in bins, I calculate total number of balls accepted by bins
for i in range(len(bins_new)):
    for j in range(len(bins_new[i])):
        for k in range(len(bins_new[i][j])):
            bins_new[i][j][k] = len(bins_new[i][j][k])            


# In[7]:


bins_new[14][0]


# In[8]:


# I get maximum value in each bunch of bins and because of getting one single list for all of them, 
# I divide them into 10, 20, 30, 40, 50 particular parts again using numpy
maxes = []
for i in range(len(bins_new)):
    for j in range(len(bins_new[i])):
        max_val = max(bins_new[i][j])
        maxes.append(max_val)
experiments = np.array_split(maxes, 15)


# In[9]:


experiments


# In[10]:


# I create empty lists for appending numbers from different experiments based on particular bin count
list_10 = []
list_20 = []
list_30 = []
list_40 = []
list_50 = []

for i in range(len(experiments)):
    list_10.append(experiments[i][0])
    list_20.append(experiments[i][1])
    list_30.append(experiments[i][2])
    list_40.append(experiments[i][3])
    list_50.append(experiments[i][4])
    
# By converting particular lists to numpy arrays I get particular averages to use later
ave_10 = round(np.array(list_10).mean(),2)
ave_20 = round(np.array(list_20).mean(),2)
ave_30 = round(np.array(list_30).mean(),2)
ave_40 = round(np.array(list_40).mean(),2)
ave_50 = round(np.array(list_50).mean(),2)

std_10 = round(np.array(list_10).std(ddof = 1),2)
std_20 = round(np.array(list_20).std(ddof = 1),2)
std_30 = round(np.array(list_30).std(ddof = 1),2)
std_40 = round(np.array(list_40).std(ddof = 1),2)
std_50 = round(np.array(list_50).std(ddof = 1),2)



print(f"The average of max values for 10 bins is: {ave_10}")
print(f"The average of max values for 20 bins is: {ave_20}")
print(f"The average of max values for 30 bins is: {ave_30}")
print(f"The average of max values for 40 bins is: {ave_40}")
print(f"The average of max values for 50 bins is: {ave_50}")
print("-----------------------------------------------")
print(f"The std of max values for 10 bins is: {std_10}")
print(f"The std of max values for 20 bins is: {std_20}")
print(f"The std of max values for 30 bins is: {std_30}")
print(f"The std of max values for 40 bins is: {std_40}")
print(f"The std of max values for 50 bins is: {std_50}")


# In[11]:


# I am repeating exactly same process for getting result for k = 2 case
# where we take two random bins for particular ball each time and throw the ball
# to the least occupied one

# Delivery of Balls step
bins_new2 = []
for exp in range(num_exp):
    random.seed(exp+1)
    bins2 = copy.deepcopy(bins)
    for pack in range(len(balls)):
        for ball in range(balls[pack].shape[0]):
            selected = random.choices(bins2[pack], k = 2)
            min(selected, key=len).append(balls[pack][ball])
    bins_new2.append(bins2)    
    
    
# Summing accumulated Balls step   
for i in range(len(bins_new2)):
    for j in range(len(bins_new2[i])):
        for k in range(len(bins_new2[i][j])):
            bins_new2[i][j][k] = len(bins_new2[i][j][k]) 
            
            

# Getting max values step
maxes2 = []
for i in range(len(bins_new2)):
    for j in range(len(bins_new2[i])):
        max_val2 = max(bins_new2[i][j])
        maxes2.append(max_val2)
experiments2 = np.array_split(maxes2, 15)


# Getting particular Averages step
list2_10 = []
list2_20 = []
list2_30 = []
list2_40 = []
list2_50 = []

for i in range(len(experiments2)):
    list2_10.append(experiments2[i][0])
    list2_20.append(experiments2[i][1])
    list2_30.append(experiments2[i][2])
    list2_40.append(experiments2[i][3])
    list2_50.append(experiments2[i][4])
    
ave2_10 = round(np.array(list2_10).mean(),2)
ave2_20 = round(np.array(list2_20).mean(),2)
ave2_30 = round(np.array(list2_30).mean(),2)
ave2_40 = round(np.array(list2_40).mean(),2)
ave2_50 = round(np.array(list2_50).mean(),2)

std2_10 = round(np.array(list2_10).std(ddof = 1),2)
std2_20 = round(np.array(list2_20).std(ddof = 1),2)
std2_30 = round(np.array(list2_30).std(ddof = 1),2)
std2_40 = round(np.array(list2_40).std(ddof = 1),2)
std2_50 = round(np.array(list2_50).std(ddof = 1),2)

print(f"The average of max values for 10 bins is: {ave2_10}")
print(f"The average of max values for 20 bins is: {ave2_20}")
print(f"The average of max values for 30 bins is: {ave2_30}")
print(f"The average of max values for 40 bins is: {ave2_40}")
print(f"The average of max values for 50 bins is: {ave2_50}")
print("-----------------------------------------------")
print(f"The std of max values for 10 bins is: {std2_10}")
print(f"The std of max values for 20 bins is: {std2_20}")
print(f"The std of max values for 30 bins is: {std2_30}")
print(f"The std of max values for 40 bins is: {std2_40}")
print(f"The std of max values for 50 bins is: {std2_50}")


# In[12]:


# I am repeating exactly same process for getting result for k = 4 case
# where we take four random bins for particular ball each time and throw the ball
# to the least occupied one

# Delivery of Balls step
bins_new4 = []
for exp in range(num_exp):
    random.seed(exp+1)
    bins4 = copy.deepcopy(bins)
    for pack in range(len(balls)):
        for ball in range(balls[pack].shape[0]):
            selected = random.choices(bins4[pack], k = 4)
            min(selected, key=len).append(balls[pack][ball])
    bins_new4.append(bins4)    
    
    
# Summing accumulated Balls step   
for i in range(len(bins_new4)):
    for j in range(len(bins_new4[i])):
        for k in range(len(bins_new4[i][j])):
            bins_new4[i][j][k] = len(bins_new4[i][j][k]) 
            
            

# Getting max values step
maxes4 = []
for i in range(len(bins_new4)):
    for j in range(len(bins_new4[i])):
        max_val4 = max(bins_new4[i][j])
        maxes4.append(max_val4)
experiments4 = np.array_split(maxes4, 15)


# Getting particular Averages step
list4_10 = []
list4_20 = []
list4_30 = []
list4_40 = []
list4_50 = []

for i in range(len(experiments4)):
    list4_10.append(experiments4[i][0])
    list4_20.append(experiments4[i][1])
    list4_30.append(experiments4[i][2])
    list4_40.append(experiments4[i][3])
    list4_50.append(experiments4[i][4])
    
ave4_10 = round(np.array(list4_10).mean(),2)
ave4_20 = round(np.array(list4_20).mean(),2)
ave4_30 = round(np.array(list4_30).mean(),2)
ave4_40 = round(np.array(list4_40).mean(),2)
ave4_50 = round(np.array(list4_50).mean(),2)


std4_10 = round(np.array(list4_10).std(ddof = 1),2)
std4_20 = round(np.array(list4_20).std(ddof = 1),2)
std4_30 = round(np.array(list4_30).std(ddof = 1),2)
std4_40 = round(np.array(list4_40).std(ddof = 1),2)
std4_50 = round(np.array(list4_50).std(ddof = 1),2)

print(f"The average of max values for 10 bins is: {ave4_10}")
print(f"The average of max values for 20 bins is: {ave4_20}")
print(f"The average of max values for 30 bins is: {ave4_30}")
print(f"The average of max values for 40 bins is: {ave4_40}")
print(f"The average of max values for 50 bins is: {ave4_50}")
print("-----------------------------------------------")
print(f"The std of max values for 10 bins is: {std4_10}")
print(f"The std of max values for 20 bins is: {std4_20}")
print(f"The std of max values for 30 bins is: {std4_30}")
print(f"The std of max values for 40 bins is: {std4_40}")
print(f"The std of max values for 50 bins is: {std4_50}")


# In[13]:


experiments4


# In[14]:


#Collections particular means and stds to the same list
k_1_ave = [ave_10,ave_20,ave_30,ave_40,ave_50]
k_1_std = [std_10,std_20,std_30,std_40,std_50]
k_2_ave = [ave2_10,ave2_20,ave2_30,ave2_40,ave2_50]
k_2_std = [std2_10,std2_20,std2_30,std2_40,std2_50]
k_4_ave = [ave4_10,ave4_20,ave4_30,ave4_40,ave4_50]
k_4_std = [std4_10,std4_20,std4_30,std4_40,std4_50]


# In[15]:


k_1_ave[0]


# In[16]:


k_1_std[0]


# In[17]:


# Calculating Confidence Intervals
ci_k_1 = []
ci_k_2 = []
ci_k_4 = []
q_value = 0.975     # upper limit for 95 confidence interval
for num in range(len(k_1_ave)):
        mean = k_1_ave[num]
        sigma = k_1_std[num]/math.sqrt(num_exp)   # Standard deviation estimate, len(num_exp) => Sample size
        t_value = stats.t.ppf(q = q_value, df = num_exp-1)  # Get the t-critical value
        delta = t_value * sigma                             # Margin of Error
        conf_int = (mean - delta, mean + delta)      # Calculation of Confidence Interval
        ci_k_1.append(conf_int)
        
        
# For k = 2
for num in range(len(k_2_ave)):
        mean = k_2_ave[num]
        sigma = k_2_std[num]/math.sqrt(num_exp)   # Standard deviation estimate, len(num_exp) => Sample size
        t_value = stats.t.ppf(q = q_value, df = num_exp-1)  # Get the t-critical value
        delta = t_value * sigma                             # Margin of Error
        conf_int2 = (mean - delta, mean + delta)      # Calculation of Confidence Interval
        ci_k_2.append(conf_int2)
        
        
# For k = 4      
for num in range(len(k_4_ave)):
        mean = k_4_ave[num]
        sigma = k_4_std[num]/math.sqrt(num_exp)   # Standard deviation estimate, len(num_exp) => Sample size
        t_value = stats.t.ppf(q = q_value, df = num_exp-1)  # Get the t-critical value
        delta = t_value * sigma                             # Margin of Error
        conf_int4 = (mean - delta, mean + delta)      # Calculation of Confidence Interval
        ci_k_4.append(conf_int4)
        


# In[18]:


ci_k_1


# In[19]:


ci_k_2


# In[20]:


ci_k_4


# In[21]:


# Relative Error for k = 1 case
RE_1 = []
for i in range(len(ci_k_1)):
    re1 = (ci_k_1[i][1] - k_1_ave[i])/k_1_ave[i]
    RE_1.append(re1)

# Relative Error for k = 2 case    
RE_2 = []
for j in range(len(ci_k_2)):
    re2 = (ci_k_2[j][1] - k_2_ave[j])/k_2_ave[j]
    RE_2.append(re2)


# Relative Error for k = 4 case    
RE_4 = []
for z in range(len(ci_k_4)):
    re4 = (ci_k_4[z][1] - k_4_ave[z])/k_4_ave[z]
    RE_4.append(re4)


# In[22]:


RE_1


# In[23]:


RE_2


# In[24]:


RE_4


# In[25]:


# Visualizing Relative Error
fig = plt.figure()
plt.figure(figsize=(8,6))
plt.scatter(bins_balls, RE_1, color = "blue" , label = "RE of d = 1 condition")
plt.plot(bins_balls, RE_1, color = "blue", linewidth=2)
plt.plot(bins_balls, RE_2 ,color = "red", linewidth=2)
plt.scatter(bins_balls, RE_2, color = "red", label = "RE of d = 2 condition")
plt.plot(bins_balls, RE_4, color = "green", linewidth=2)
plt.scatter(bins_balls, RE_4, color = "green", label = "RE of d = 4 condition")
plt.xlabel("Number of Bins and Balls")
plt.ylabel("Relative Error")
plt.legend(loc = "upper right")
#plt.title("Relative Errors with respect to dropping condition")
plt.show()
fig.savefig('Relative errors', dpi=500)


# In[26]:


x = bins_balls
y_up = []
y_low = []
for i in range(5):
    y1 = ci_k_1[i][1]
    y2 = ci_k_1[i][0]
    y_up.append(y1)
    y_low.append(y2)
    
max_oc = []
for j in range(len(bins_balls)):
    maxes = math.log(bins_balls[j])/math.log(math.log(bins_balls[j]))*2
    max_oc.append(maxes)
    
fig, ax = plt.subplots(figsize=(8,6))
ax.fill_between(x, y_up, y_low, alpha=0.4, linewidth=0, label = "Confidence interval")
ax.plot(x, k_1_ave, linewidth=2)
ax.scatter(x, k_1_ave, color = "blue", label = "Average max occupancy")
ax.plot(x, max_oc, linewidth=2)
ax.scatter(x, max_oc, color = "orange", label = "Theorithical max occupancy")
plt.legend(loc = "lower right")
plt.xlabel("Number of Bins and Balls")
plt.ylabel("Maximum Occupancy")
#plt.title("k = 1 dropping condition")


# In[27]:


y_up2 = []
y_low2 = []
for i in range(5):
    y1 = ci_k_2[i][1]
    y2 = ci_k_2[i][0]
    y_up2.append(y1)
    y_low2.append(y2)
    
max_oc2 = []
for j in range(len(bins_balls)):
    maxes = math.log(math.log(bins_balls[j]))/math.log(2)
    max_oc2.append(maxes)
    
fig, ax = plt.subplots(figsize=(8,6))
ax.fill_between(x, y_up2, y_low2, alpha=0.4, linewidth=0, label = "Confidence interval")
ax.plot(x, k_2_ave, linewidth=2)
ax.scatter(x, k_2_ave, color = "blue", label = "Average max occupancy")
ax.plot(x, max_oc2, linewidth=2)
ax.scatter(x, max_oc2, color = "orange", label = "Theorithical max occupancy")
plt.legend(loc = "lower right")
plt.xlabel("Number of Bins and Balls")
plt.ylabel("Maximum Occupancy")
#plt.title("k = 2 dropping condition")


# In[28]:


y_up4 = []
y_low4 = []
for i in range(5):
    y1 = ci_k_4[i][1]
    y2 = ci_k_4[i][0]
    y_up4.append(y1)
    y_low4.append(y2)
    
max_oc4 = []
for j in range(len(bins_balls)):
    maxes = math.log(math.log(bins_balls[j]))/math.log(4) 
    max_oc4.append(maxes)
    
fig, ax = plt.subplots(figsize=(8,6))
ax.fill_between(x, y_up4, y_low4, alpha=0.4, linewidth=0, label = "Confidence interval")
ax.plot(x, k_4_ave, linewidth=2)
ax.scatter(x, k_4_ave, color = "blue", label = "Average max occupancy")
ax.plot(x, max_oc4, linewidth=2)
ax.scatter(x, max_oc4, color = "orange", label = "Theorithical max occupancy")
plt.legend(loc = "lower right")
plt.xlabel("Number of Bins and Balls")
plt.ylabel("Maximum Occupancy")
#plt.title("k = 4 dropping condition")


# In[ ]:





# In[ ]:





# In[ ]:




