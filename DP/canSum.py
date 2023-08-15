#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:50:56 2022

@author: muntazirabidi
"""


def canSum(targetSum, arr, memo={}):
    
    if targetSum in memo.keys(): return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False
    
    for num in arr:
        remainder = targetSum - num
        if canSum(remainder, arr, memo) == True:
            memo[targetSum] = True
          
            return True
        
    memo[targetSum] = False
    
    return False
    
    
#print(canSum(7,[2,3]))
#print(canSum(7,[5,3,4,7]))
#print(canSum(7,[2,4]))
#print(canSum(8,[2,3,5]))
print(canSum(7071,[7,14]))
