#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 23:49:51 2022

@author: muntazirabidi
"""

def canConstruct(target, wordBank, memo=None):
    if memo == None: memo = {}
    if target in memo: return memo[target]
    if target == '': return True
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
        else:
            pass
    memo[target] = False
    return False
        
    



print(canConstruct('aabbc',['aa','bb','c']))


print(canConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd']))

print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))

print(canConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))

print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee',
                                                            'eeeee', 'eeeeee']))