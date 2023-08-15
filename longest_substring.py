#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:59:35 2022

@author: muntazirabidi
"""
#----------(1)-----------------------
# The conplexity of this code is O(N^3)
def lengthOfLongestSubstring1(s):
    def check(start, end):
        chars = [0]*128
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] +=1
       
            if chars[ord(c)] > 1:
                return False
        return True
    
    res = 0;
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            print(i,j, check(i,j))
            if check(i,j):
                res = max(res, j-i+1)
    return res


#------------------(2)-----------------------
    # The conplexity of this code is O(N)

def lengthOfLongestSubstring(s):
    ans = 0
    i=0;
    n = len(s);
    mp = {};
    
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)
            
        ans = max(ans, j-i+1)
        mp[s[j]] = j + 1
        
    return ans

s = 'bbbbb'
s= "abcabcbb"
s = "pwwkew"
print(lengthOfLongestSubstring(s))