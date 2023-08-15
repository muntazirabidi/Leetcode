#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 01:03:52 2022

@author: muntazirabidi
"""

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
          
            profit = profit+ max(prices[i]-prices[i-1], 0)
     
        return profit

prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices =  [1,2,1,3,4,9,9,1,13]
sol = Solution()
print(sol.maxProfit(prices))