#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:21:54 2022

@author: muntazirabidi
"""
# Iterative solution
def depthFirstPrint(graph, source):
    stack = [source]
    
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        
        for neighbour in graph[current]:
            stack.append(neighbour)
    
def depthFirstPrint2(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrint2(graph, neighbour)
    

                   
            
            
graph = {'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [] }


depthFirstPrint(graph, 'a')