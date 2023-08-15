#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:02:16 2022

@author: muntazirabidi
"""

def shortesPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set([nodeA])
    queue = [[nodeA,0]];
    
    
    while len(queue) != 0:
        [node, distance] = queue.pop(0)
        
        if node == nodeB : return distance
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour, distance + 1])
    return -1
    
    
    
def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a,b] = edge
        if a not in graph.keys(): graph[a] = []
        if b not in graph.keys(): graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
        
    return graph
            
            
    
    

edges = [
        ['w', 'x'],
        ['w', 'v'],
        ['x', 'y'],
        ['y', 'z'],
        ['v','z']
        ]

print(buildGraph(edges)  )
print(shortesPath(edges, 'w', 'z'))