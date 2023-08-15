#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:29:04 2022

@author: muntazirabidi
"""

class Solution:
    def isHappy(self, n):
        if n != 1 and len(str(n)) == 1:
            return False
        
        def square_sum(n):
            s = str(n)
            sqr_sum = 0
            for i in range(len(s)):
                sqr_sum = sqr_sum  + int(s[i])**2
                
            return sqr_sum
        
        seen = set()
            
        while n != 1 and n not in seen:
            seen.add(n)
            n = square_sum(n)
            
        return n == 1
            
            
  
    
    



n = 75
sol = Solution()
print(sol.isHappy(n))