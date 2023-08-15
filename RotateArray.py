#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:56:35 2022

@author: muntazirabidi
"""

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            #print(i, nums[i], a,(i + k) % n)
            
        nums[:] = a
        return nums
        
        
        
def rotate2(nums, k):
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]
    return nums
        
nums = [1,2,3,4,5,6,7];
k = 3
Output: [5,6,7,1,2,3,4];

#sol = Solution()
#print(sol.rotate(nums, k))

print(rotate2(nums, k))
    