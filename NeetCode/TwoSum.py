#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:51:33 2022

@author: muntazirabidi
"""

class Solution(object):
    def twoSum(self,numbers, target):

     for num in numbers:
            
            L, R = 0, len(numbers) - 1
            
            while True:
                sums = numbers[L] + numbers[R]
                
                if sums < target:
                    L += 1
                elif sums > target:
                    R -= 1
                else:
                    return [L+1, R+1]
                    
        
        
        
        
        
        
sol = Solution()
numbers = [2,7,11,15]
target = 9

print(sol.twoSum(numbers, target))