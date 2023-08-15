#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:26:49 2022

@author: muntazirabidi
"""

def ismatch(text, pattern):
    if not pattern: return not text
    
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    
    
    return first_match and ismatch(text[1:], pattern[1:])
    

# - '.' Matches any single character.​​​​
# - '*' Matches zero or more of the preceding element.
text = "aa";
pattern = "a*";

text = "aa";
pattern = "a*";

#text = "ab";
#pattern = ".*"

print(ismatch(text, pattern))