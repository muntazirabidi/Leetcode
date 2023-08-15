#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:32:35 2022

@author: muntazirabidi
"""

class Solution:
    def maxArea_brute(self, height):
        max_area = 0
        for i in range(len(height)): 
            for j in range(i+1, len(height)):     
                width = abs(i - j)
                max_area = max(max_area, min(height[j],height[i])*width)
                    
        return max_area
            
            
        
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) -1 
        
        while left < right:
            width = right - left
            max_area = max(max_area, min(height[right], height[left])*width)
            
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
                
        return max_area
        
        
height = [1,8,6,2,5,4,8,3,7]

        
height2 = [1,1]

sol = Solution()

print(sol.maxArea_brute(height))

print(sol.maxArea(height))

