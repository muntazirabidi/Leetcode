#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:13:19 2022

@author: muntazirabidi
"""

def searchX(matrix, x):
    n = len(matrix)
    m = len(matrix[0])
    if n==0 or m ==0:
        return -1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == x:
                print('Elemnet found at (',i,', ', j,')')
                
                return 1
            
    print('Element not found')
    return 0
            
            
    

# Python3 program to search an element
# in row-wise and column-wise sorted matrix
 
# Searches the element x in mat[][]. If the
# element is found, then prints its position
# and returns true, otherwise prints "not found"
# and returns false
def search(mat, n, x):
 
    i = 0
     
    # set indexes for top right element
    j = n - 1
    while ( i < n and j >= 0 ):
     
        if (mat[i][j] == x ):
     
            print('Elemnet found at (',i,', ', j,')')
            return 1
     
        if (mat[i][j] > x ):
            j -= 1
             
        # if mat[i][j] < x
        else:
            i += 1
     
    print("Element not found")
    return 0 # if (i == n || j == -1 )
    
    
    
    
matrix = [ [10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50]]

x = 29


print(searchX(matrix, x))

print(search(matrix, 4,x))