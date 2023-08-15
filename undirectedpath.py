#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:33:16 2022

@author: muntazirabidi
"""

def undirectedPath(edges, nodeA, nodeB):
    graph = buildgraph(edges)
    return haspath(graph, nodeA, nodeB, set([]))
        
  
def haspath(graph, src, dst, visited):
    if src in visited: return False
    
    if src == dst: return True
    
    visited.add(src)
    
    for neighbour in graph[src]:
        if haspath(graph, neighbour, dst, visited) == True:
            return True
    return False   

def buildgraph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge
        if a not in graph: graph[a] = [];
        if b not in graph: graph[b] = [];
        
        graph[a].append(b)
        graph[b].append(a)
        
    return graph
            
        



edges = [['i','j'], ['k','i'], ['m','k'], ['k','l'], ['o','n']]
graph = buildgraph(edges)
print(graph)
src = 'l'
dst = 'o'


print(undirectedPath(edges, src, dst))