#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:35:47 2022

@author: muntazirabidi
"""

#Longest Consecutive Sequence 

class Solution:
    def longestConsecutive_bruteforce(self, nums):
        
        longest_streak = 0
        
        for num in nums:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
        return longest_streak
    
    
    def longestConsecutive(self, nums):
        
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
    
        return longest_streak
    
nums = [100, 4, 200, 1,3,2]

nums = [0,3,7,2,5,8,4,6,0,1]

sol = Solution()

print(sol.longestConsecutive_bruteforce(nums))

print(sol.longestConsecutive(nums))





