#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:35:27 2022

@author: muntazirabidi
"""


def ConnectedComponentsCount(graph):
    visited = set([])
    count =0;
    for node in graph:
        print(visited)
        if explore(graph, node, visited) == True: count += 1
        
    return count


def explore(graph, current, visited):
    if current in visited : return False
    
    visited.add(current)
    
    for neighbour in graph[current]:
        explore(graph, neighbour, visited)
        
    return True
    

graph= {
        3:[],
        4:[6],
        6:[4,5,7,8],
        8:[6],
        7:[6],
        6:[6],
        1:[2],
        2:[1]
    
        }

graph= {
        0:[8,1,5],
        1:[0],
        5:[0,8],
        8:[0,5],
        2:[3,4],
        3:[2,4],
        4:[3,2]
    
        }

print(ConnectedComponentsCount(graph))