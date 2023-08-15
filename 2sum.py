#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:00:44 2022

@author: muntazirabidi
"""
# Brute force O(N^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                print(i,j)
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None 
    
# efficient : O(N)
class Solution2:
    def twoSum(self, nums, target) :
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            #print(complement, hashmap)
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
    
nums = [3,2,4];
target = 6  
sol = Solution()
#print(sol.twoSum(nums, target))

sol = Solution2()
print(sol.twoSum(nums, target))