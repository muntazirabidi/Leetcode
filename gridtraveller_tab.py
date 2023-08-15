#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:17:43 2022

@author: muntazirabidi
"""

def gridtraveller(m,n):
    d = [[1] * (n) for _ in range(m)]

    
    for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]
            
    
    return d[m-1][n-1]


print(gridtraveller(3,3))
