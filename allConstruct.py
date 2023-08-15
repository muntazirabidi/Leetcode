#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:34:48 2022

@author: muntazirabidi
"""



def allConstruct(target, wordBank, memo = None):
    if memo == None: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]
    
    result  = []
    
    for word in wordBank:
       if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix , wordBank, memo)
            targetWays = list(map(lambda way: [word, *way],suffixWays))
            result.append(targetWays)
            memo[target] = result
  
            
    memo[target]= result
    return result
            

def allConstruct(target, wordBank, memo = None):
    if memo == None: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]
    result  = []
    for word in wordBank:
       if target.find(word) == 0:
            # Remove word from beginning of target
            new_target = target[len(word):]
            suffix_ways = allConstruct(new_target, wordBank,memo)
            for way in suffix_ways:
                way.insert(0, word) 
            result.extend(suffix_ways)  # Extend!
            memo[target] = result

    memo[target] = result
    return result


print(allConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd', 'c']))
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee',
                                                            'eeeee', 'eeeeee']))