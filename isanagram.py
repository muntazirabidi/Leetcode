#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:26:59 2022

@author: muntazirabidi
"""

def isAnagaram(s1,s2):
    if len(s1) != len(s2): return False
    hash_table1 = {}
    hash_table2 = {}
    for i in range(len(s1)):
        if s1[i] in hash_table1:
            hash_table1[s1[i]] = hash_table1[s1[i]] + 1
        else:
            hash_table1[s1[i]] = 1
    
    for i in range(len(s2)):
        if s2[i] in hash_table2:
            hash_table2[s2[i]] = hash_table2[s2[i]] + 1
        else:
            hash_table2[s2[i]] = 1
        
    if hash_table1 == hash_table2:
        return True
    
    else:
        return False
    
from collections import Counter
def isAnagaram2(s1,s2):
    if len(s1) != len(s2): return False
    return Counter(s1.lower()) == Counter(s2.lower())
    
s1 = 'Debitcard'
s2 = 'Badcredit'
print(isAnagaram2(s1,s2))
print(Counter(s1.lower()))
print(Counter(s2.lower()))
    