#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:06:04 2022

@author: muntazirabidi
"""

def fib(n):
    table = [0]*(n+1)
    table[0] = 1
    table[1] = 1

    for i in range(0,n-1):

        table[i+1] += table[i]
        table[i+2] += table[i]
    
    
    return table[n]
    
print(fib(100))
print(fib(6))
print(fib(7))
print(fib(8))