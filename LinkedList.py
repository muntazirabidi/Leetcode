#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:09:20 2022

@author: muntazirabidi
"""
class Node:
    '''
    An objetct for storing a single node in a linked list
    
    Attributes:
        data: Data stored in a node 
        next_node: Reference to the next node in linked list
    '''
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Nodes data: %s>" % self.data
    

class SinglyLinkedList:
    '''
    Linear data structure that store values in nodes. The List
    maintains a reference to the first node, also called head, 
    Each node points to the next node in the List
    
    Attributes:
        head: The head node of the list
    '''
    def __init__(self):
        self.head = None
        self.__count = 0
        
    def is_empty(self):
        '''
        determines if the linked list is empty or not
        O(1) time complexity
        '''

        return self.head == None
    
    def __len__(self):
        return self.__count
    
    def add(self, data):
        '''
        Adds new Node containing data to head of the list.
        Takes O(1) time
        '''
        new_head = Node(data, next_node=self.head)
        self.head = new_head
        self.__count += 1
        
    def search(self, key):
        current = self.head
        
        while current:
            if current.data == key: 
                return current
            else:
                current = current.next_node
                
        return None
            
        
    