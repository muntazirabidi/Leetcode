#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:07:30 2022

@author: muntazirabidi
"""

def howSum(targetSum, arr, memo = None):
    if memo is None : memo = {}
    if targetSum in memo.keys(): return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    for num in arr:
        remainder = targetSum - num
        remainderResult = howSum(remainder, arr, memo)
        
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]
   
          
    

    memo[targetSum] = None
    return None
    
    
print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(7071,[7,14]))
