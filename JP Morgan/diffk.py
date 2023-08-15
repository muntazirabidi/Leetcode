#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:14:05 2022

@author: muntazirabidi
"""
from collections import Counter


def findpairs_diffK(nums,k):
    result = 0
    counter = Counter(nums)
        
    for x in counter:
          
        if k > 0 and x + k in counter:
             result += 1
        elif k == 0 and counter[x] > 1:
             result += 1
    return result




arr  = [1,7,5,9,2,12,3]
k=2

# -> {(1,3), (3,5), (5,7), (7,9)}

print(Counter(arr))
findpairs_diffK(arr,k)