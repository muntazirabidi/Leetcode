#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:59:01 2022

@author: muntazirabidi
"""

from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):

        return list((Counter(nums1) & Counter(nums2)).elements())



nums1 = [4,9,5];
nums2 = [9,4,9,8,4]



print(Counter(nums1))
print(Counter(nums2))

print((Counter(nums1) & Counter(nums2)))
print(list((Counter(nums1) & Counter(nums2))))


set1 = set(nums1)
set2 = set(nums2)

print(list(set1.intersection(set2)))