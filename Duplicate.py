#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:28:31 2022

@author: muntazirabidi
"""

#Given an integer array nums, return true if any value appears at least twice in the array, 
#and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                hash_table[nums[i]] = hash_table[nums[i]] + 1
            
                return True
            else:
                hash_table[nums[i]] = 1

        return False
        
        
class Solution2:
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


class Solution3:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) >= 2:
                return True
        return False
    
class Solution4:
    def containsDuplicate(self, nums):
        return True if len(set(nums)) < len(nums) else False
            
            
        
nums = [1,2,3,1]
sol = Solution4()
res = sol.containsDuplicate(nums)
print(res)