#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:24:26 2022

@author: muntazirabidi
"""

class Solution():
    def isPalindrome(self, s):
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)
        
        filtered_chars_list = list(lowercase_filtered_chars)
        revered_chars_list = filtered_chars_list[::-1]
        
        return filtered_chars_list == revered_chars_list

     def isPalindrome_pointers(self, s):
         i,j = 0, len(s) -1
         
         while i < j:
             while i < j and not s[i].isalnum():
                 i += 1
             while i < j and not s[j].isalnum():
                 j -= 1
            
             if s[i].lower() != s[j].lower():
                return False
            
             i += 1
             j -= 1
            
        return True
    
    
     def isPalindrome2(self, s):
         s = ''.join(ch.lower() for ch in s if ch.isalnum())
         
         return True is s == s[::-1] else False
         
         
         
         
         

            


s = "A man, a plan, a canal: Panama"


sol = Solution()

print(sol.isPalindrome(s))

print(sol.isPalindrome2(s))

print(sol.isPalindrome_pointers(s))




