#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:26:31 2022

@author: muntazirabidi
"""

#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets

class Solution:
    def threeSum(self, nums):
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
                        
         
        
nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))


res, dups = set(), set()
seen = {}
for i, val1 in enumerate(nums):
    if val1 not in dups:
        dups.add(val1)
        for j, val2 in enumerate(nums[i+1:]):
            complement = -val1 - val2
            if complement in seen and seen[complement] == i:
                res.add(tuple(sorted((val1, val2, complement))))
            seen[val2] = i