#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:35:10 2022

@author: muntazirabidi
"""

def islandCount(grid):
    visited = set([]);
    count = 0;
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r,c, visited) == True: 
                count += 1 # toDo
            
            
    return count



def explore(grid, r,c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])
    if not rowInbounds and not colInbounds: return False
    
    if grid[r][c] == 'W': return False
    
    pos = str(r)+','+str(c)
    if pos in visited: return False
    
    visited.add(pos)
    
    
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)
    
    return True # just finished exploring a brand new island.
    


Grid = [
        ['W', 'L','W','W','L','W'],
        ['L', 'L','W', 'W', 'L', 'W'],
        ['W', 'L', 'W','W','W','W'],
        ['W','W','W','L', 'L','W'],
        ['W','L','W','L', 'L', 'W'],
        ['W','W','W','W','W','W']
        ]


print(islandCount(Grid))