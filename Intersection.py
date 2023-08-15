#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 23:32:54 2022

@author: muntazirabidi
"""

class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        hash_table = {}
        for i in range(len(nums1)):
                if nums1[i] in hash_table:
                    hash_table[nums1[i]] = hash_table[nums1[i]] + 1
                else:
                    hash_table[nums1[i]] = 1
                    
        res = []
        for j in range(len(nums2)):
            if nums2[j] in hash_table and hash_table[nums2[j]] >= 1:
                res.append(nums2[j])
                hash_table[nums2[j]] = hash_table[nums2[j]]  - 1
        return res

                    
       
        
        
        
nums1 = [4,9,5,4,4];
nums2 = [9,4,9,8,4];
sol = Solution()
print(sol.intersect(nums1, nums2))