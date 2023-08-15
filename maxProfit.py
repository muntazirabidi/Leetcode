#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 01:14:49 2022

@author: muntazirabidi
"""

class Solution:
    def maxProfit2(self, prices):
        profit = 0
        
        for i in range(1, len(prices)):
            
            profit = profit + max(prices[i] - prices[i-1], 0)
            
        return profit
    
    
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
    
    
prices = [7,1,5,3,6,4]

sol = Solution()
print(sol.maxProfit(prices))