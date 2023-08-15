#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:01:40 2022

@author: muntazirabidi
"""

class Solution(object):
    def strStr(self, haystack, needle):
        #haystack_len = len(haystack)
        #needle_len = len(needle)
        
        #first_letter = needle[0]
        #first_occurence = -1
        
        if needle.strip()=='':
            return 0
        
        if needle in haystack:
        
            return haystack.find(needle)
        else:
            return -1
        #for i in range(haystack_len):
            
        
        
        
haystack = "hello";
needle = "ll"

sol = Solution()
print(sol.strStr(haystack, needle))

if needle in haystack:
    print(haystack.find(needle))
    print('true')