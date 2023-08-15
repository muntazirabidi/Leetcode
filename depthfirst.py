#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:39:06 2022

@author: muntazirabidi
"""
# Going to be a Stack

# Iterative solution
def depthfirst(graph, source):
    stack = [source]
    
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        
        for neighbour in graph[current]:
            stack.append(neighbour)
    

def depthfirst2(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthfirst2(graph, neighbour)
    

        

graph = {'a': ['c','b'],
              'b': ['d'],
              'c': ['e'],
              'd': ['f'],
              'e': [],
              'f': []
             
                  }


print(depthfirst2(graph, 'a'))
print(depthfirst(graph, 'a'))