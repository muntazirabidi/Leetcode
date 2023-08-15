#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:41:27 2022

@author: muntazirabidi
"""

def intToRoman(num):
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        for value, symbol in digits:
            
            if num == 0: break
            
            count, num = divmod(num, value)
            
   
            roman_digits.append(symbol * count)
            #print(roman_digits, count, symbol * count, symbol)
        
        return ''.join(roman_digits)
        
        
print(intToRoman(11))

print(intToRoman(71))

print(intToRoman(1994))