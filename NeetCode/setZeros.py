#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:44:01 2022

@author: muntazirabidi
"""

class Solution:
    def setZeroes(self, matrix):
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        rows, cols = set(), set()
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                    
                    
        return matrix
    

matrix = [[1,1,1],[1,0,1],[1,1,1]]

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()

print(sol.setZeroes(matrix))

print(sol.setZeroes(matrix2))