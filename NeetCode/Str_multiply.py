#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:10:14 2022

@author: muntazirabidi
"""

class Solution:
    def multiply(self, num1, num2):
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        results = []
        
        for index, digit in enumerate(second_number):
            result.append(self.miltiply_one_digit(digit, indexm first_number))
            
            
    def multiply_one_digit(self, digit, num_zeros, first_number):
        current_result = [0]*num_zeros
        carry = 0
        for digit in first_number:
            multiplication = int(digit1)* int(digit2) + carry
            carry = multiplication // 10
            
            current_result.append(multiplication % 10)
            
            if carry != 0:
                current_result.append(carry)
                
            return current_result
            
num1 = "123"
num2 = "456"
sol = Solution()

print(sol.multiply(num1, num2))