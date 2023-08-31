#!/usr/bin/env python
# coding: utf-8

# # Task 1.2

# Derive measures of
# 1. Probability that the server is IDLE
# 2. Probability that the DELAY is below a given value
# 3. Distribution of the number of USERS

# In[1]:


import matplotlib.pyplot as plt
import random
from queue import PriorityQueue
from datetime import datetime
import numpy as np


# In[2]:


class Measure:
    def __init__(self,Narr,Ndep,NAveraegUser,OldTimeEvent,AverageDelay):
        self.arr = Narr
        self.dep = Ndep
        self.ut = NAveraegUser
        self.oldT = OldTimeEvent
        self.delay = AverageDelay


# In[3]:


class Client:
    def __init__(self,type,arrival_time):
        self.type = type
        self.arrival_time = arrival_time


# In[4]:


count = []             # for counting how many times newcoming user has not encountered with someone in the queue
def arrival(time, FES, queue):
    global users
            
    # cumulate statistics
    data.arr += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time

    # sample the time until the next arrival
    inter_arrival = random.expovariate(lambd=1.0/ARRIVAL)
    
    # schedule the next arrival
    FES.put((time + inter_arrival, "arrival"))

    # update the state variable, by increasing the no. of clients by 1
    users += 1
    
    # create a record for the client
    client = Client(TYPE1,time)

    # insert the record in the queue
    queue.append(client)

    # if the server is idle start the service
    if users==1:
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        # schedule the departure of the client
        FES.put((time + service_time, "departure"))
        count.append(1)   # <---------------------------------------


# In[5]:


Delays_list = []     #<------------

def departure(time, FES, queue):
    global users

    # get the first element from the queue
    client = queue.pop(0)
        
    # cumulate statistics
    data.dep += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time
    
    Delays_list.append(time-client.arrival_time)   # append each delay to list
    data.delay += (time-client.arrival_time)


    # update the state variable, by decreasing the no. of clients by 1
    users -= 1
    
    # check whether there are more clients to in the queue
    if users >0:
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        # schedule the departure of the client
        FES.put((time + service_time, "departure"))


# In[6]:


# get the start time
start_time = datetime.now()

Num_departures = []
Arrivals = []
Idle = []

Loads = []
Delays = []
Theo_del = []
for i in range(20):
    #arrivals=0
    users=0                                    # State variable: number of users
    time = 0.                                  # the simulation time 
    queue=[]                                   # Queue of the clients
    data = Measure(0,0,0,0,0)                  # Collect measurements
    FES = PriorityQueue()                      # Future Event Set: the list of events in the form: (time, type)
    FES.put((0, "arrival"))                    # schedule the first arrival at t=0
    random.seed(40)                            # Initialize the random number generator    

    load = 0.5 + i*(0.95-0.5)/20               # load of the queue
    Loads.append(load)
    SERVICE = 10.0                             # av service time
    ARRIVAL   = SERVICE/load                   # av. inter-arrival time
    TYPE1 = 1                                  # At the beginning all clients are of the same type, TYPE1 

    SIM_TIME = 500000                           # condition to stop the simulation

    while time < SIM_TIME:
    # Extract next event from the FES
        (time, event_type) = FES.get()
    # Call the event functions based on the event type 
        if event_type == "arrival":
            #print("length of queue before",len(queue))
            arrival(time, FES, queue)
           

        elif event_type == "departure":
            departure(time, FES, queue)

    #theorical_user = (1.0/ARRIVAL)/(1.0/SERVICE-1.0/ARRIVAL)  # Average number of users - Theoritical

    theorical_delay = 1.0/(1.0/SERVICE-1.0/ARRIVAL)  # Average delay - Theoritical
    Theo_del.append(theorical_delay)

    Delays.append(data.delay/data.dep)
    #print(data.dep)
    Num_departures.append(data.dep)  # Departures for each load which is useful to separate delays per load
    
    #print(len(count), data.arr)
    Idle.append(len(count))
    Arrivals.append(data.arr)

# get the end time
end_time = datetime.now()
# get the execution time
print('Duration: {}'.format(end_time - start_time))


# In[7]:


Num_departures


# In[8]:


# Separating counts of each load
Idles_arr = np.insert(np.diff(Idle), 0, Idle[0])
# Probability of Idles per each load
prob = Idles_arr/Arrivals*100


# In[9]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(Loads, prob, color = "blue", label = "Idle")
plt.plot(Loads, prob, linewidth=2)
plt.legend(loc = "upper right")
plt.xlabel("Loads")
plt.ylabel("Probability")


# In[10]:


len(Delays_list)


# In[11]:


Delays_split = [Delays_list[sum(Num_departures[:i]):sum(Num_departures[:i+1])] for i in range(len(Num_departures))]


# In[12]:


# I check the percentage of Delay smaller than 40 units of time for each Load
def percentage(l):
    count = 0
    for i in l:
        if i < 40:
            count = count + 1
    percent = round(count/len(l), 3)
    return percent


# In[13]:


per_list = []
for i in range(len(Delays_split)):
    per = percentage(Delays_split[i])
    per_list.append(per)    


# In[14]:


per_list


# In[15]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(Loads, per_list, color = "blue", label = "Prob < 40 units of time")
plt.plot(Loads, per_list, linewidth=2)
plt.legend(loc = "upper right")
plt.xlabel("Loads")
plt.ylabel("Probability")


# In[ ]:




