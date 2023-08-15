#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:57:51 2022

@author: muntazirabidi
"""

def kth_largest(arr, k):
    for i in range(k-1):
        #arr.pop(arr.index(max(arr)))
        arr.remove(max(arr))
        
    return max(arr)
    
def kth_largest2(arr, k):
    arr = sorted(arr)
    for i in range(k-1):
        return arr[n-k]   
    
import heapq  
def kth_largest3(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

    
arr = [4,2,9,7,5,6,7,1,3]
k = 4;

print(kth_largest3(arr, k))