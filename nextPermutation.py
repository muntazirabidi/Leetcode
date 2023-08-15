#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:45:48 2022

@author: muntazirabidi
"""

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2;
        while i >=0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >=0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
            
        self.reverse(nums, i+1)
        
        return nums
        
    def reverse(self, nums, start):
        i = start
        j = len(nums)-1
        while i <j:
            self.swap(nums, i,j)
            i += 1
            j -= 1
        
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        
nums = [1,2,3]
sol = Solution()
print(sol.nextPermutation(nums))