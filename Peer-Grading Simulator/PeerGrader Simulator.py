#!/usr/bin/env python
# coding: utf-8

# In[289]:


import numpy as np
import matplotlib.pyplot as plt
import math 
import random
import scipy.stats as stats


# In[290]:


# Enter Number of Students, Homeworks and Evaluators
stud = input("Number of students: ")  #defined 20
hmw = input("Number of homeworks: ")  #defined 20
k = input("Number of evaluators: ")   #defined [4,5,6,7,8,9,10] to see change in errors


# In[291]:


stud = np.zeros(int(stud))
hmw = np.zeros(int(hmw))
k = np.zeros(int(k))


# In[292]:


# Generate random values between 0 and 1 to show Quality of each student
# 1 dimensional array
np.random.seed(8111996)
Xs = np.zeros(stud.shape[0])
for i in range(stud.shape[0]):
    Xs[i] = np.random.uniform(0,1)
    Xs[i] = round(Xs[i], 2)


# In[293]:


Xs.shape


# In[294]:


# Generate random values between 0 and 1 to show Quality of particular Homework for particular Student
# 2 dimensional array
Qhs = np.zeros((hmw.shape[0], Xs.shape[0]))
np.random.seed(8111996)
for h in range(hmw.shape[0]):
    for i in range(Xs.shape[0]):
        mean = Xs[i]                   
        std=0.1
        Qhs[h][i] = np.random.normal(loc=mean, scale=std)
        Qhs[h][i] = round(Qhs[h][i], 4)
        if Qhs[h][i]<0:
            Qhs[h][i]=0
        if Qhs[h][i]>1:
            Qhs[h][i]=1        


# In[295]:


Qhs.shape


# In[296]:


# Generate random values between 0 and 1 to show Evaluation of particular Evaluator for particular Homework of 
# particular Student ---> 3 dimensional array
Ehs = np.zeros((k.shape[0], hmw.shape[0], Xs.shape[0]))
np.random.seed(8111996)
for h in range(hmw.shape[0]):
    for i in range(Xs.shape[0]):
        for e in range(k.shape[0]):
            mean = Qhs[h][i]
            std = 0.1
            Ehs[e][h][i] = np.random.normal(loc = mean, scale = std)
            Ehs[e][h][i] = round(Ehs[e][h][i], 4)
            if Ehs[e][h][i]<0:
                Ehs[e][h][i]=0
            if Ehs[e][h][i]>1:
                Ehs[e][h][i]=1


# In[297]:


Ehs.shape


# In[298]:


# With simple numpy function we get Estimated Quality of particular Homework for particular Student
# by taking average of evaluations for particular Homework for particular Student
Qhs_hat = np.average(Ehs, axis=0)
for h in range(Qhs_hat.shape[0]):
    for i in range(Qhs_hat.shape[0]):
        Qhs_hat[h][i] = round(Qhs_hat[h][i], 4)


# In[300]:


Qhs_hat.shape


# In[266]:


# By exploiting features of numpy library we calculate Average Relative Grading Error (homework-by-homework)
diff = Qhs_hat - Qhs
diff = np.absolute(diff)
Epsilon1 = np.average(diff)
Epsilon1 = round(Epsilon1, 4)


# In[267]:


Epsilon1


# In[268]:


# With same strategy we Average Relative Grading Error (final grade)
Sum_diff = np.sum(diff, axis = 0)
Sum_qhs = np.sum(Qhs, axis = 0)
Sum_diff_s = np.sum(Sum_diff)
Sum_qhs_s = np.sum(Sum_qhs)
Epsilon2 = Sum_diff_s/Sum_qhs_s/stud.shape[0]
Epsilon2 = round(Epsilon2, 4)


# In[269]:


Epsilon2


# stud ---> 20 --> 20 --> 20 --> 20 --> 20 --> 20 -->20
# 
# hmw  ---> 20 --> 20 --> 20 --> 20 --> 20 --> 20 -->20
# 
# k    ---> 4  --> 5  --> 6  --> 7  --> 8  --> 9  -->10
# 
# Epsilon1 = (0.0396,0.0326,0.0333,0.0319,0.0305,0.0277,0.0262)
# 
# Epsilon2 = (0.0044,0.0036,0.0037,0.0036,0.0034,0.0031,0.0029)

# In[270]:


#Results obtained from simulations
k_list = [4,5,6,7,8,9,10]
e1 = [0.0396,0.0326,0.0333,0.0319,0.0305,0.0277,0.0262]
e2 = [0.0044,0.0036,0.0037,0.0036,0.0034,0.0031,0.0029]


# In[287]:


#Visualizing error1
fig = plt.figure()
plt.plot(k_list, e1)
plt.xlabel("number of evaluators")
plt.ylabel("error 1 - homework-by-homework")
plt.show()
fig.savefig('e1', dpi=300)


# In[288]:


#Visualizing error2
fig = plt.figure()
plt.plot(k_list, e2)
plt.xlabel("number of evaluators")
plt.ylabel("error 2 - final grade")
plt.show()
fig.savefig('e2', dpi=300)


# In[ ]:





# In[ ]:





# In[ ]:




