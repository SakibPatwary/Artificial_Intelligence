#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random

location = ['A','B']

status = ['Clean','Dirty']

print('\nTask1\n')

table = {

    ('A','Dirty'):'suck',

    ('A','Clean'):'right',

    ('B','Dirty'):'suck',

    ('B','Clean'):'left'

}

percepts = []



def table_driven_agent(percept):

    percepts.append(percept)

    action = table.get(percept)

    return action

def simple_reflex_agent (percept):
    location= percept[0]

    status= percept[1]
    if status=='Dirty':
        print('suck')
    elif location=='A':
        print('right')
    else:
        print('left')

for i in range(4):

    l = random.choice(location)

    s = random.choice(status)

    percept = (l,s)

    action = table_driven_agent(percept)

    print(action)


print('\nTask2\n')
for i in range(4):

    l = random.choice(location)

    s = random.choice(status)

    percept = (l,s)
    simple_reflex_agent(percept)
    


# In[ ]:




