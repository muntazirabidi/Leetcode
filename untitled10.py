#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:32:11 2022

@author: muntazirabidi
"""

def factorial(n):
    if n==0 or n==1 : return 1
    
    return n*factorial(n-1)
    

def handshake(n):
    # Write your code here
    return factorial(n)/(factorial(2)*factorial(n-2))