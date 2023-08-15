#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:00:10 2022

@author: muntazirabidi
"""

queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print('Initial queue')
print(queue)

print('Elements dequeued from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('Queue after removing elements')