#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 01:26:47 2022

@author: muntazirabidi
"""

class Solution:
    def maxProduct(self, nums):
        current_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            current_subarray = max(num, current_subarray * num)
            max_subarray = max(max_subarray, current_subarray)
            
        return max_subarray
    
    
    
nums = [2,3,-2,4]

nums = [-2,0,-1]

sol = Solution()

print(sol.maxProduct(nums))