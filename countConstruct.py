#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:24:12 2022

@author: muntazirabidi
"""



def countConstruct(target, wordBank, memo=None):
    if memo == None: memo = {}
    if target in memo: return memo[target]
    if target == '' : return 1 
    
    total_count = 0
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            numWaysforRest = countConstruct(suffix , wordBank, memo)
            total_count = total_count + numWaysforRest
            
    memo[target] = total_count
    return total_count
    

print(countConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd', 'c', 'a', 'ef']))
print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))

print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee',
                                                            'eeeee', 'eeeeee']))