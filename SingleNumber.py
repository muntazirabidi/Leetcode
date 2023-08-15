#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:59:27 2022

@author: muntazirabidi
"""

class Solution:
    def singleNumber(self, nums):
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                hash_table[nums[i]] = hash_table[nums[i]] + 1
            else:
                hash_table[nums[i]] = 1
                
        for k,v in hash_table.items():
            if v == 1:
                return k
            
                
class Solution2(object):
    def singleNumber(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()        

        
        
        
        
        
nums = [1, 1, 2, 2, 4]
sol = Solution2()
res = sol.singleNumber(nums)
print(res)