#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:43:23 2022

@author: muntazirabidi
"""
def zeroPad(numberString, zeros, left = True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def multiply(num1, num2):
    x = num1
    y = num2
    """Multiply two integers using Karatsuba's algorithm."""

    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    #for odd digit integers
    if (n % 2) != 0:
        j += 1    
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    
    #recursively calculate
    ac = multiply(str(a), str(c))
    bd = multiply(str(b), str(d))
    k = multiply(str(a+b), str(c + d))
    print(ac)
    A = int(zeroPad(ac, AZeroPadding, False))

    B = int(zeroPad(str(int(k) - int(ac) - int(bd)), BZeroPadding, False))
    return str(A + B + bd)

num1='23'
num2='334'
print(multiply(num1, num2))