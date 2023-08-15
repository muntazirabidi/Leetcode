#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:06:24 2022

@author: muntazirabidi
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def sum_list(head):
  if head is None: return 0
  sum_list = 0
  while head is not None:

    sum_list += head.val
    head = head.next
    
  return sum_list


def linked_list_find(head, target):
    if head is None: return False
    
    while head is not None:
        if head.val == target : return True
        head = head.next
        
    return False

a = Node('A')
b = Node("B")
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


x = Node(38)
y = Node(4)

x.next = y

print(sum_list(x))


print(linked_list_find(a, "C")) # True