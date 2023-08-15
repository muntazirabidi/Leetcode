#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:31:43 2022

@author: muntazirabidi
"""

def isPalindrome(x):
    num_string = str(x)
    n = len(num_string)
    
    print(num_string, n)
    i,j=0,n-1
    for k in range(n//2):
        if num_string[i] == num_string[j]:
            i += 1
            j -= 1
            print(i,j)
        else:
            return False
    return True
    
    
x=123210
x=113
print(isPalindrome(x))