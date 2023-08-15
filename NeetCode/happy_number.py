#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:56:23 2022

@author: muntazirabidi
"""

class Solution:
    def isHappy(self, n):
        if n!=1 and len(str(n)) == 1:
            return False
        
        def square_sum(n):
            s = str(n)
            sqr_sum = 0
            for i in range(len(s)):
                sqr_sum = sqr_sum + int(s[i])**2
                
            return sqr_sum
        
        seen  =set()
        
        while n!=1 and n not in seen:
            seen.add(n)
            n = square_sum(n)
            
        return n==1

            

sol = Solution()

n=19
print(sol.isHappy(n))