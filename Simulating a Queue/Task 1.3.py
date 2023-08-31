#!/usr/bin/env python
# coding: utf-8

# # Task 1.3 

# Modify the simulator and assume a finite capacity B of the waiting line. Measure:
# 
# 1. Probability that a customer is lost
# 2. Average delay 

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


#lost_clients = []  
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
    
            
    if users < 6:   # at most 6 clients in front of arrival
        # update the state variable, by increasing the no. of clients by 1
        users += 1
        # create a record for the client
        client = Client(TYPE1,time)
        # insert the record in the queue
        queue.append(client)
    else:
        lost_clients.append(1)
        
            

    # update the state variable, by increasing the no. of clients by 1
    #users += 1
    
    # create a record for the client
    #client = Client(TYPE1,time)

    # insert the record in the queue
    #queue.append(client)

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


# In[6]:


# get the start time
start_time = datetime.now()


chunks = []
lost_clients = [] 

num_queue = []                                 # Num Arrivals
arr_load = []                                  # Num Arrivals per load
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
    

    #num_queue = []
    #arr_load = []
    while time < SIM_TIME:


    # Extract next event from the FES
        (time, event_type) = FES.get()
    # Call the event functions based on the event type 
        if event_type == "arrival":
            #print(len(queue))
            # New arrival comes and sees how many customer is in queue
            #num_queue.append(len(queue))
            arrival(time, FES, queue)


            #print(len(lost_clients))

        elif event_type == "departure":
            departure(time, FES, queue)
                    
    #print(len(lost_clients))


    chunks.append(len(lost_clients))   #<---------------------------------

    arr_load.append(data.arr)
    #print(data.arr)
    #theorical_user = (1.0/ARRIVAL)/(1.0/SERVICE-1.0/ARRIVAL)  # Average number of users - Theoritical

    theorical_delay = 1.0/(1.0/SERVICE-1.0/ARRIVAL)  # Average delay - Theoritical
    Theo_del.append(theorical_delay)

    Delays.append(data.delay/data.dep)
    #print(len(queue))
    
# get the end time
end_time = datetime.now()
# get the execution time
print('Duration: {}'.format(end_time - start_time))


# In[7]:


chunks


# In[8]:


arr_load


# In[9]:


per_list = []
for i in range(20):
    per = round(chunks[i]/arr_load[i]*100,3)
    per_list.append(per)


# In[10]:


per_list


# In[11]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(Loads, per_list, color = "blue", label = "Lost probability")
plt.plot(Loads, per_list, linewidth=2)
plt.legend(loc = "upper left")
plt.xlabel("Loads")
plt.ylabel("Probability")


# In[12]:


Delays


# In[13]:


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(Loads, Delays, color = "blue", label = "Average Delay")
plt.plot(Loads, Delays, linewidth=2)
plt.legend(loc = "upper left")
plt.xlabel("Load")
plt.ylabel("Time")


# In[ ]:




