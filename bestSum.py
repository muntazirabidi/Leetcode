#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 23:22:43 2022

@author: muntazirabidi
"""

def bestSum(target_sum, numbers, memo = None):

    if memo == None: memo = {}
    
    if target_sum in memo: return memo[target_sum]
    
    if target_sum < 0: return None
        
    if target_sum == 0 : return []

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num

        remainder_combination = bestSum(remainder, numbers, memo)
        if remainder_combination != None:
            remainder_combination.append(num)
            if shortest_combination == None or len(remainder_combination) < len(shortest_combination):
                shortest_combination = remainder_combination
                
    memo[target_sum] = shortest_combination
    return shortest_combination
    
    
    
    
print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8,[1,4,5,3,7,8]))
print(bestSum(100,[1,2,5,25]))