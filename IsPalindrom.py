#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:11:44 2022

@author: muntazirabidi
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
       
        
        return True if s == s[::-1] else False

s = "A man, a plan, a canal: Panama"


sol = Solution()
print(sol.isPalindrome(s))


print(s)
s = ''.join(ch.lower() for ch in s if ch.isalnum())
#s = ''.join(filter(str.isalnum, s))
print(s)
rev_str = s[::-1]
print(rev_str)