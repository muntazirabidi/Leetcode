#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:56:05 2022

@author: muntazirabidi
"""
from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        hash_table = Counter(s)
        n = len(s)
        
                
        for i in range(n):
            if s[i] in hash_table and hash_table[s[i]] == 1:
               
                return i
        
      
        return -1
    
    
    
s = "leetcode"
s="loveleetcode"

sol = Solution()
print(sol.firstUniqChar(s))
for idx, ch in enumerate(s):
    print(idx,ch)

count = Counter(s)
print(count)