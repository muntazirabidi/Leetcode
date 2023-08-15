#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:10:57 2022

@author: muntazirabidi
"""


# breadthfirst solution
def has_path(graph, source, dst):
    queue = [source]
    
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst : return True 
        for neighbour in graph[current]:
            queue.append(neighbour)
    
    return False


# Iterative Solution
def has_path2(graph, source, dst):
    if source == dst: return True 
    for neighbour in graph[source]:
        if has_path(graph, neighbour, dst) == True:
            return True
    return False




    

graph = {'f': ['g', 'i'],
         'g': ['h'],
         'h': [],
         'i': ['g', 'k'], 
         'j': ['i'],
         'k': []}

source = 'h'
dst = 'k'

print(has_path(graph, source, dst))

print(has_path2(graph, source, dst))

