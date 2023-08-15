#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:26:49 2022

@author: muntazirabidi
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_list = {}
        for i in range(len(nums)):
            if nums[i] in hash_list:
                hash_list[nums[i]] = hash_list[nums[i]] + 1
            else:
                hash_list[nums[i]] = 1
        for i, v in enumerate(sorted(hash_list)):
            nums[i] = v
        
        return i+1
        
        
nums = [1,1,2,3]     
nums= [0,0,1,1,1,2,2,3,3,4]   
sol = Solution()
res = sol.removeDuplicates(nums)

print(res)

