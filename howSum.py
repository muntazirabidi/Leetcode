#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:20:58 2022

@author: muntazirabidi
"""
# m = target sum
# n = lentgh of the array

# time: O(n^m * m) without memorization / Brute Force
# Space : O(m)

# with memorisation the time complexity is O(n * m^2)
# space O(m^2)

def howSum(targetSum, nums, memo = None): 

    if memo is None:
        memo = {}
        
    if targetSum in memo: return memo[targetSum]
    if targetSum < 0: return None
    if targetSum == 0: return []
    
    for num in nums:
        remainder = targetSum - num
        remainderResult = howSum(remainder, nums , memo) #pass memo as well
        
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]
        
    memo[targetSum] = None
    return None

print(howSum(7, [2, 3])) # [3,2,2]
print(howSum(7, [5, 3, 4, 7])) # [4,3]
print(howSum(7, [2, 4])) # None
print(howSum(8, [2, 3, 5])) # [2,2,2,2]
print(howSum(23, [15,4,2,3])) # None
 
