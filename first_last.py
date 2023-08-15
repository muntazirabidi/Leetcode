#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:37:10 2022

@author: muntazirabidi
"""

# Given a sorted array of integers arr and an integer target, find the index of the first and last poisiton of target in arr. 
# If target can't be found in arr return [-1,-1]


def index_first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
        
    return [-1,-1]
    
def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right=mid -1
            
    return -1

def first_and_last(arr, target):
    if len(arr) == 0 : return [-1,-1]
    start = find_start(arr, target)
    if start == -1 : return [-1,1]
    
    end = start
    while end +1 < len(arr) and arr[end+1] == target:
        end +=1
    return [start, end]
    
    
arr = [2,4,5,5,5,5,5,7,9,9]
target = 5

output = [2,6]

print(find_start(arr, target))

print(index_first_and_last(arr, target))
print(first_and_last(arr, target))
