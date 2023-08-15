#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:24:02 2022

@author: muntazirabidi
"""
import numpy as np

def FindMissingNumber(nums):
    N = len(nums) + 1
    total = N*(N+1)/2
    
    return total - np.sum(nums)
    