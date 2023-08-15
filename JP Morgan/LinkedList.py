#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:13:17 2022

@author: muntazirabidi
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def push(self, new_data):
        new_node = Node(new_data)
        
        new_node.next = self.head
        self.head  = new_node
        
        
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printList()



def rotateLeft(d, arr):
    rotated_arr = []
    for i in range(len(arr)):
        rotated_arr.append(arr[(i+d)%len(arr)])
    return rotated_arr

arr = [1,2,3,4,5,5,6]
d = 2
print(rotateLeft(d, arr))
