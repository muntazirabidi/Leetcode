#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:13:44 2022

@author: muntazirabidi
"""

class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        return self.gridTraveler(m,n)
    
    def gridTraveler(self,  m,n):
        
        if m == 1 and n ==1: return 1
            
        if n == 0 or m == 0: return 0
        
        return self.gridTraveler(n-1, m) + self.gridTraveler(n,m-1)
        
    
        
        
    #def minPathSum(self, grid):
    #   return self.calculate(grid, 0,0)
    
    #def calculate(self,grid, i,j):
    #    print(grid[i][j])

    #   if i == len(grid) - 1 and j == len(grid[0]) -1:
    #      return grid[i][j]
    #  else:
    #     return grid[i][j] + min(self.calculate(grid, i+1, j), self.calculate(grid, i,j+1))
        
        
        
        
grid = [[1,3,1],[1,5,1],[4,2,1]]

sol = Solution()
print(sol.minPathSum(grid))
