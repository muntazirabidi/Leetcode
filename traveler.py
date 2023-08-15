#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:45:04 2022

@author: muntazirabidi
"""

# Say that you are a traveler on a 2D grid. You begin in the top-left corner 
# and your goal is to travel to the bottom-right corner. You may only move down or right. 
# In how many ways can you travel to the goal on a grid with dimensions $m*n$.
 
def gridtraveler(m,n):
    if n ==0 or m==0:
        return 0
    
    if n==1 and m==1:
        return 1
    
    return gridtraveler(m-1,n) + gridtraveler(m,n-1)
    



print(gridtraveler(1,2))
print(gridtraveler(5,10))


# ========== using memorization ======
def gridtraveler2(m,n, memo={}):
    # are the arguments in the memo
    key = str(m) + ',' + str(n)
    if key in memo.keys():
        return memo[key]

    if n ==0 or m==0:
        return 0
    
    if n==1 and m==1:
        return 1
    
    memo[key] = gridtraveler2(m-1,n, memo) + gridtraveler2(m,n-1,memo)
 
    return memo[key]
    



print(gridtraveler2(3,2))
print(gridtraveler2(180,180))