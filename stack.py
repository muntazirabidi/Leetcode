#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:49:13 2022

@author: muntazirabidi
"""

# Last in first out
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)

print('Elements popped from Stack')

print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Stack after elements are popped:')
print(stack)