#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:20:32 2022

@author: muntazirabidi
"""
# ======= Classical Recursion Problem =============
def fib(n):
    if n <=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

print(fib(6))
print(fib(10))

# ============== Dynammic Programming ================
# ----memorization

def fib_new(n, memo = {}):
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib_new(n-1, memo) + fib_new(n-2, memo)
    return memo[n]
    
print(fib_new(6))
print(fib_new(50))