#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:59:36 2022

@author: muntazirabidi
"""

def largestComponent(graph):
    longest = 0
    visited = set([])
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest: longest = size
        
    return longest


def exploreSize(graph, node, visited):
    if node in visited : return 0
    
    visited.add(node)
    
    size = 1;
    
    for neighbour in graph[node]:
        size += exploreSize(graph, neighbour, visited)
        
    return size


graph= {
        0:[8,1,5],
        1:[0],
        5:[0,8],
        8:[0,5],
        2:[3,4],
        3:[2,4],
        4:[3,2]
    
        }

print(largestComponent(graph))