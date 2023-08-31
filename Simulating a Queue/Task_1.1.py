#!/usr/bin/env python
# coding: utf-8

# # Task 1.1

# Plot graphs of the average DELAY vs LOAD given by --> Average_Service_Time/Average_InterarrivalTime
# 
# 1. Observe impact of simulation
# 2. Try and change the seed

# In[1]:


import matplotlib.pyplot as plt
import random
from queue import PriorityQueue
from datetime import datetime


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


# In[5]:


def departure(time, FES, queue):
    global users

    # get the first element from the queue
    client = queue.pop(0)
        
    # cumulate statistics
    data.dep += 1
    data.ut += users*(time-data.oldT)
    data.oldT = time
    data.delay += (time-client.arrival_time)


    # update the state variable, by decreasing the no. of clients by 1
    users -= 1
    
    # check whether there are more clients to in the queue
    if users >0:
        # sample the service time
        service_time = random.expovariate(1.0/SERVICE)
        # schedule the departure of the client
        FES.put((time + service_time, "departure"))


# In[15]:


# get the start time
start_time = datetime.now()

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

    SIM_TIME = 5000000                           # condition to stop the simulation

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

# get the end time
end_time = datetime.now()
# get the execution time
print('Duration: {}'.format(end_time - start_time))


# In[7]:


Delays


# In[8]:


# seed 40, sim_time = 50000, t = 00.55 second
l1 = Loads
d1 = Delays
td1 = Theo_del
print(l1)
print(d1)
print(td1)


# In[11]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(l1, d1, color = "blue", label = "Average Delay")
ax.scatter(l1, td1, color = "orange", label = "Theoritical")
plt.plot(l1, d1, linewidth=2)
plt.plot(l1, td1, linewidth=2)
plt.legend(loc = "upper left")
plt.xlabel("Loads")
plt.ylabel("Time")


# In[13]:


# seed 40, sim_time = 500000, t = 05.28 second 
l2 = Loads
d2 = Delays
td2 = Theo_del


# In[14]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(l2, d2, color = "blue", label = "Average Delay")
ax.scatter(l2, td2, color = "orange", label = "Theoritical")
plt.plot(l2, d2, linewidth=2)
plt.plot(l2, td2, linewidth=2)
plt.legend(loc = "upper left")
plt.xlabel("Loads")
plt.ylabel("Time")


# In[16]:


# seed 40, sim_time = 5000000, 01 minute 52.29 second
l3 = Loads
d3 = Delays
td3 = Theo_del


# In[17]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(l3, d3, color = "blue", label = "Average Delay")
ax.scatter(l3, td3, color = "orange", label = "Theoritical")
plt.plot(l3, d3, linewidth=2)
plt.plot(l3, td3, linewidth=2)
plt.legend(loc = "upper left")
plt.xlabel("Loads")
plt.ylabel("Time")


# In[ ]:




