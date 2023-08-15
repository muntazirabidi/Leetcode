#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 01:31:03 2022

@author: muntazirabidi
"""

class Solution:
    def fib(self, n, memo = {}):
        if n in memo.keys():
            return memo[n]
        
        if n <= 2:
            return 1
   
        else: 
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]
        
        
sol  = Solution()

n=40
print(sol.fib(n))