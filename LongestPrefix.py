#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:12:28 2022

@author: muntazirabidi
"""
class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return p

class Solution:
    def longestCommonPrefix(self, strs):
 
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break 
        return "".join(prefix)


strs = ["flower","flow","flight"]

sol = Solution()
print(sol.longestCommonPrefix(strs))

print(strs)


for x in zip(*strs):
    print(x)
    print(set(x))