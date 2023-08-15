#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 00:42:27 2022

@author: muntazirabidi
"""


class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                return nums[i:] + nums[:i]
        return nums
        

class Solution2:
    def moveZeroes(self, nums):
 
        pos = 0
        
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

nums = [0,1,0,3,12,0,4,3,0]
sol = Solution()
print(sol.moveZeroes(nums))
        