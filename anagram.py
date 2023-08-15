#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:55:45 2022

@author: muntazirabidi
"""
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        counter_s = Counter(s)
        counter_t = Counter(t)
        
        if counter_s == counter_t:
            return True
        else:
            return False
            


s = "anagram";
t = "nagaram";
sol = Solution()
sol.isAnagram(s,t)
print(sorted(s))
print(sorted(s))