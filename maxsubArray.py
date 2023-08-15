#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 00:57:46 2022

@author: muntazirabidi
"""
import math

class Solution:
    def maxSubArrayB(self, nums):
        max_subarray = -math.inf
        
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
                
        return max_subarray
    
    def maxSubArray(self, nums):
        current_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
            
        return max_subarray
    
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]
sol = Solution()
print(sol.maxSubArrayB(nums))

print(sol.maxSubArray(nums))

print(sol.maxSubArrayB(nums2))