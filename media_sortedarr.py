#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:51:48 2022

@author: muntazirabidi
"""

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).
class Solution(object):

    def findMedianSortedArrays(self, A,B):

        median = 0;
        C  = A + B
        C.sort()


        if len(C) % 2 == 1:
            median = C[len(C)//2]
        else:
            median = (C[len(C)//2] + C[len(C) // 2 - 1])/2

        return median


A = [1,2]
B= [4,3]
sol = Solution()

median = sol.findMedianSortedArrays(A,B)
print(median)
