#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 01:16:59 2022

@author: muntazirabidi
"""

s = ["h","e","l","l","o"]
s= ["H","a","n","n","a","h"]

n = len(s)
i=0
j=n-1
for i in range(len(s) // 2):
    s[i], s[j] = s[j], s[i]
    i = i+1
    j= j-1
    print(s, i,j)
print(s)