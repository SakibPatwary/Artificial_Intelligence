#!/usr/bin/env python
# coding: utf-8

# In[1]:


graph={

    'S':{'A':5,'B':2,'C':4},
    
    'A':{'D':9,'E':4},
    
    'B':{'G':6},
    
    'C':{'F':2},
    
    'D':{'H':7},
    
    'E':{'G':6},
    
    'F':{'G':1},
    
    'G':{},
    
    'H':{}
    
    }

from queue import PriorityQueue


def Uniform_Cost_Search(startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}

    pq = PriorityQueue()
    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        distance[node] = -1

    startingPoint = startingNode
    visited[startingPoint] = True
    distance[startingPoint] = 0
    pq.put((0, startingPoint))

    while not pq.empty():
        u = pq.get()[1]

        if u == destinationNode:
            break
        visited[u] = True
        for v in graph[u].keys():
            if not visited[v]:
                parent[v] = u
                distance[v] = distance[u] + graph[u][v]
                pq.put((distance[v], v))

    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]
    path.reverse()
    print(path)
    print(distance[destinationNode])

Uniform_Cost_Search('S','G')


# In[ ]:




