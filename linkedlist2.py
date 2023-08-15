#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:47:10 2022

@author: muntazirabidi
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

def printlist(head):
    if head is None: return 
    print(head.val)
    printlist(head.next)

def linked_list_values(head):
  return_arr = []
  current = head
  while current is not None:
    return_arr.append(current.val)
    current = current.next
    
  return return_arr

a = Node('A')
b = Node("B")
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

print(linked_list_values(a))