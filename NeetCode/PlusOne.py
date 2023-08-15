#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:59:30 2022

@author: muntazirabidi
"""

class Solution:
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
        
        
sol = Solution()

digits = [9,9]
print(sol.plusOne(digits))