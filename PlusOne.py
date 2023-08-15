#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 00:06:36 2022

@author: muntazirabidi
"""

#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.


        
class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            print(i)
            carry, digits[i] = divmod(carry + digits[i],10)
        
        print(digits)
        if(carry ==0):
            return digits
        
        return [1] + digits
        
        
class Solution3:
    def plusOne(self, digits):
        num = int("".join(str(e) for e in digits))
        print(num)
        num2 = num + 1
        res = [int(i) for i in str(num2)]
        return res
    
class Solution2:
    def plusOne(self, digits):
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
          
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits
        
    
digits = [123]
sol = Solution3()
print(sol.plusOne(digits))