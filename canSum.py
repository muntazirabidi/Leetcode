#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:21:22 2022

@author: muntazirabidi
"""

#Write  a function that takes in a targetSum and an array of numbers as arguments.

#The function should return a boolean indicating whether or not it is possible 
#to generate the targetSum using numbers from the array. 

#You may use an element of the array as many times as needed. 

#you may assume that all input numbers are non-negative.

# canSum(7, [4,2])--> false
# canSum(7, [5,3,4,7]) --> True

def canSum(targetSum, arr):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in arr:
        remainder = targetSum - num
        if canSum(remainder, arr) == True:
            return True
    
    return False
    
    
#print(canSum(7,[2,3]))
#print(canSum(7,[5,3,4,7]))
#print(canSum(7,[2,4]))
#print(canSum(8,[2,3,5]))
#print(canSum(300,[7,14]))


#=========== Memorisation ==========

def canSum2(targetSum, arr, memo={}):
    
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in arr:
        remainder = targetSum - num
        if canSum2(remainder, arr, memo) == True:
            memo[targetSum] = True
          
            return True
        
    memo[targetSum] = False
    
    return False
    
    
#print(canSum2(7,[2,3]))
#print(canSum2(7,[5,3,4,7]))
#print(canSum2(7,[2,4]))
#print(canSum2(8,[2,3,5]))
print(canSum2(7071,[7,14]))


