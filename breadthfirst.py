#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:59:28 2022

@author: muntazirabidi
"""


def breadthfirst(graph, source):
    
    queue = [source]
    
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)
    
    


graph = {'a': ['c','b'],
              'b': ['d'],
              'c': ['e'],
              'd': ['f'],
              'e': [],
              'f': []
                  }

breadthfirst(graph, 'a')