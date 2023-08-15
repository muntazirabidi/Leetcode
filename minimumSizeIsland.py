#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:00:26 2022

@author: muntazirabidi
"""


                
            

def exploreSize(grid, r,c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])
    if not rowInbounds and not colInbounds: return 0
    
    # What if the position is water?
    if grid[r][c] == 'W' : return 0
    
    pos = str(r)+','+str(c)
    
    if pos in visited: return 0
    
    visited.add(pos)
    
    size=1;
    size += exploreSize(grid, r-1,c,visited)
    size += exploreSize(grid, r+1,c,visited)
    size += exploreSize(grid, r,c-1,visited)
    size += exploreSize(grid, r+1,c,visited)
    
    return size

def minimumIsland(grid):
    visited = set([]);
    minimumSize = float('inf');
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSize(grid, r,c, visited)
             
            if size > 0 and size < minimumSize: minimumSize = size
            
    return minimumSize



Grid = [
        ['W', 'L','W','W','L','W'],
        ['L', 'L','W', 'W', 'L', 'W'],
        ['W', 'L', 'W','W','W','W'],
        ['W','W','W','L', 'L','W'],
        ['W','L','W','L', 'L', 'W'],
        ['W','W','W','W','W','W']
        ]

print(minimumIsland(Grid))